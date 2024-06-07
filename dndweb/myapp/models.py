from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .spell_slots import bard_spell_slots, cleric_spell_slots, druid_spell_slots, paladin_spell_slots, ranger_spell_slots, sorcerer_spell_slots, warlock_spell_slots, wizard_spell_slots, artificer_spell_slots
import os, random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)  # Normalize the email address by lowercasing the domain part of it.
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True, default='username')
    email = models.EmailField(unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default_avatar.jpeg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="user_set_custom",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_set_custom",
        related_query_name="user",
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


class Rarity(models.Model):
    NONE = "არცერთი"
    COMMON = 'უბრალო'
    UNCOMMON = 'უჩვეულო'
    RARE = 'იშვიათი'
    VERY_RARE = 'ძალიან იშვიათი'
    LEGENDARY = 'ლეგენდარული'
    ARTEFACT = 'არტეფაქტი'
    CHOICES = [
        (NONE, 'არცერთი'),
        (COMMON, 'უბრალო'),
        (UNCOMMON, 'უჩვეულო'),
        (RARE, 'იშვიათი'),
        (VERY_RARE, 'ძალიან იშვიათი'),
        (LEGENDARY, 'ლეგენდარული'),
        (ARTEFACT, 'არტეფაქტი'),
    ]

    name = models.CharField(max_length=20, choices=CHOICES, unique=True)

    def __str__(self):
        return self.name

class Armor(models.Model):
    LIGHT = 'Light'
    MEDIUM = 'Medium'
    HEAVY = 'Heavy'
    NONE = 'None'
    WEIGHT_CLASS_CHOICES = [
        (LIGHT, 'Light'),
        (MEDIUM, 'Medium'),
        (HEAVY, 'Heavy'),
        (NONE, 'None'),
    ]
    name = models.CharField(max_length=50)
    armor_class = models.IntegerField()
    plus_dex_modifier = models.BooleanField(default=False)
    plus_dex_modifier_max_2 = models.BooleanField(default=False)
    strength_requirement = models.IntegerField(null=True, blank=True)
    stealth_disadvantage = models.BooleanField(default=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    cost_in_gold = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE)
    weight_class = models.CharField(max_length=10, choices=WEIGHT_CLASS_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Dice(models.Model):
    name = models.CharField(max_length=10)
    sides = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class DamageType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=50)
    cost = models.CharField(max_length=20)
    number_of_dice = models.PositiveIntegerField()
    dice = models.ForeignKey(Dice, on_delete=models.CASCADE, default=1)
    damage_types = models.ManyToManyField(DamageType)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    properties = models.ManyToManyField('Property')
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    weapon_type = models.CharField(max_length=10, choices=[('simple', 'Simple'), ('martial', 'Martial')], blank=True)
    range_type = models.CharField(max_length=10, choices=[('melee', 'Melee'), ('ranged', 'Ranged')], blank=True)

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class AbilityScore(models.Model):
    ABILITY_SCORE_CHOICES = [
        ('STR', 'Strength'),
        ('DEX', 'Dexterity'),
        ('CON', 'Constitution'),
        ('INT', 'Intelligence'),
        ('WIS', 'Wisdom'),
        ('CHA', 'Charisma'),
    ]
    
    abbreviation = models.CharField(max_length=3, choices=ABILITY_SCORE_CHOICES, unique=True)

    def __str__(self):
        return dict(self.ABILITY_SCORE_CHOICES)[self.abbreviation]

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    ability_score = models.ForeignKey(AbilityScore, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SavingThrow(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    school = models.CharField(max_length=50)
    casting_time = models.CharField(max_length=50)
    range = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    components = models.CharField(max_length=50)
    description = models.TextField()
    at_higher_levels = models.TextField(blank=True) 
    classes_using = models.ManyToManyField('Class', blank=True) 

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return self.name

class Feat(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    prerequisites = models.CharField(max_length=200, blank=True)
    benefits = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    age = models.TextField()
    size = models.TextField()
    speed = models.IntegerField()
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    traits = models.ManyToManyField('Trait', blank=True)
    languages = models.ManyToManyField('Language', blank=True)

    def __str__(self):
        return self.name

class Subrace(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    race = models.ForeignKey('Race', on_delete=models.CASCADE, null=True)
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    traits = models.ManyToManyField('Trait', blank=True)

    def __str__(self):
        return self.name

class ProficiencyBonus(models.Model):
    bonus = models.IntegerField()
    level_start = models.IntegerField()
    level_end = models.IntegerField()

    def __str__(self):
        return f"+{self.bonus} (Levels {self.level_start}-{self.level_end})"

class Proficiency(models.Model):
    name = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    proficiency_bonus = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Trait(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.IntegerField(default=0)
    proficiencies = models.ManyToManyField(Proficiency, blank=True)
    spells = models.ManyToManyField('Spell', blank=True)

    def __str__(self):
        return self.name

class SpellSlots(models.Model):
    class_name = models.CharField(max_length=50)
    level_1 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_2 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_3 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_4 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_5 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_6 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_7 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_8 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_9 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_10 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_11 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_12 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_13 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_14 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_15 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_16 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_17 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_18 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_19 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    level_20 = models.CharField(max_length=100, default='0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0')

    def __str__(self):
        return f"{self.class_name} Spell Slots"

class WeaponCategory(models.Model):
    CATEGORY_CHOICES = [
        ('simple', 'Simple'),
        ('martial', 'Martial'),
    ]
    TYPE_CHOICES = [
        ('melee', 'Melee'),
        ('ranged', 'Ranged'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.get_category_display()} {self.get_type_display()}"

class WeaponGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    weapons = models.ManyToManyField(Weapon, related_name='groups')

    def __str__(self):
        return self.name

class ArmorGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    armors = models.ManyToManyField(Armor, related_name='groups')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    cost = models.CharField(max_length=20, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class EquipmentOption(models.Model):
    name = models.CharField(max_length=100)
    weapons = models.ManyToManyField('Weapon', blank=True)
    armors = models.ManyToManyField('Armor', blank=True)
    tools = models.ManyToManyField('Tool', blank=True)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    weapon1 = models.ForeignKey('Weapon', related_name='equipments1', on_delete=models.SET_NULL, null=True, blank=True)
    weapon2 = models.ForeignKey('Weapon', related_name='equipments2', on_delete=models.SET_NULL, null=True, blank=True)
    weapon3 = models.ForeignKey('Weapon', related_name='equipments3', on_delete=models.SET_NULL, null=True, blank=True)

    weapon_group1 = models.ForeignKey('WeaponGroup', related_name='equipments1', on_delete=models.SET_NULL, null=True, blank=True)
    weapon_group2 = models.ForeignKey('WeaponGroup', related_name='equipments2', on_delete=models.SET_NULL, null=True, blank=True)
    weapon_group3 = models.ForeignKey('WeaponGroup', related_name='equipments3', on_delete=models.SET_NULL, null=True, blank=True)

    armor1 = models.ForeignKey('Armor', related_name='equipments1', on_delete=models.SET_NULL, null=True, blank=True)
    armor2 = models.ForeignKey('Armor', related_name='equipments2', on_delete=models.SET_NULL, null=True, blank=True)
    armor3 = models.ForeignKey('Armor', related_name='equipments3', on_delete=models.SET_NULL, null=True, blank=True)

    armor_group1 = models.ForeignKey('ArmorGroup', related_name='equipments1', on_delete=models.SET_NULL, null=True, blank=True)
    armor_group2 = models.ForeignKey('ArmorGroup', related_name='equipments2', on_delete=models.SET_NULL, null=True, blank=True)
    armor_group3 = models.ForeignKey('ArmorGroup', related_name='equipments3', on_delete=models.SET_NULL, null=True, blank=True)

    tool1 = models.ForeignKey('Tool', related_name='equipments1', on_delete=models.SET_NULL, null=True, blank=True)
    tool2 = models.ForeignKey('Tool', related_name='equipments2', on_delete=models.SET_NULL, null=True, blank=True)
    tool3 = models.ForeignKey('Tool', related_name='equipments3', on_delete=models.SET_NULL, null=True, blank=True)

    equipment_option1 = models.ForeignKey('EquipmentOption', related_name='equipments1', on_delete=models.SET_NULL, null=True, blank=True)
    equipment_option2 = models.ForeignKey('EquipmentOption', related_name='equipments2', on_delete=models.SET_NULL, null=True, blank=True)
    equipment_option3 = models.ForeignKey('EquipmentOption', related_name='equipments3', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    hit_die = models.ForeignKey(Dice, on_delete=models.CASCADE)
    hit_points_at_first_level = models.CharField(max_length=50, null=True, blank=True)
    hit_points_at_higher_levels = models.CharField(max_length=50, null=True, blank=True)
    saving_throw_proficiencies = models.ManyToManyField('SavingThrow')
    armor_proficiencies = models.ManyToManyField('Armor', blank=True)
    weapon_proficiencies = models.ManyToManyField('Weapon', blank=True)
    tool_proficiencies = models.ManyToManyField('Tool', blank=True)
    skill_proficiencies = models.ManyToManyField('Skill')
    weapon_groups = models.ManyToManyField('WeaponGroup', blank=True)
    armor_groups = models.ManyToManyField('ArmorGroup', blank=True)
    equipment = models.ManyToManyField('Equipment', blank=True)
    spellcasting_ability = models.ForeignKey('AbilityScore', on_delete=models.CASCADE, null=True, blank=True, related_name='spellcasting_ability_for')
    traits = models.ManyToManyField('Trait', blank=True)

    def __str__(self):
        return self.name

class Subclass(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    dnd_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subclasses')
    traits = models.ManyToManyField('Trait', blank=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    subrace = models.ForeignKey(Subrace, on_delete=models.CASCADE, null=True, blank=True)
    dnd_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subclass = models.ForeignKey(Subclass, on_delete=models.CASCADE, null=True, blank=True)
    level = models.PositiveIntegerField(default=1)
    experience_points = models.PositiveIntegerField(default=0)
    hit_points = models.PositiveIntegerField()
    max_hit_points = models.PositiveIntegerField()
    temporary_hit_points = models.PositiveIntegerField(default=0)
    armor_class = models.PositiveIntegerField()
    initiative = models.IntegerField()
    speed = models.PositiveIntegerField()
    alignment = models.CharField(max_length=50)
    background = models.CharField(max_length=100)
    proficiency_bonus = models.IntegerField()
    strength = models.PositiveIntegerField()
    dexterity = models.PositiveIntegerField()
    constitution = models.PositiveIntegerField()
    intelligence = models.PositiveIntegerField()
    wisdom = models.PositiveIntegerField()
    charisma = models.PositiveIntegerField()
    saving_throws = models.ManyToManyField(SavingThrow)
    skills = models.ManyToManyField(Skill)
    languages = models.ManyToManyField(Language)
    proficiencies = models.ManyToManyField(Proficiency)
    equipment = models.ManyToManyField(Equipment)
    spells = models.ManyToManyField(Spell)
    features = models.ManyToManyField(Trait)
    actions = models.TextField(blank=True)

    def __str__(self):
        return self.name