from django import forms

class CardFilterForm(forms.Form):
    SUPER_TYPES = [
        ('', 'Choose a Supertype'),
        ('pokemon', 'Pokemon'),
        ('trainer', 'Trainer'),
        ('energy', 'Energy'),
    ]
    supertype = forms.ChoiceField(
        choices = SUPER_TYPES,
        required = False,
        label = 'Supertype'
    )

    SERIES_CHOICES = [
        ('scarlet & violet', 'Scarlet & Violet'),
        ('sword & shield', 'Sword & Shield'),
        ('sun & moon', 'Sun & Moon'),
        ('xy', 'XY'),
        ('black & white', 'Black & White'),
        ('heartgold & soulsilver', 'HeartGold & SoulSilver'),
        ('platinum', 'Platinum'),
        ('diamond & pearl', 'Diamond & Pearl'),
        ('ex', 'EX'),
        ('base', 'Base'),
        ('other_series', 'Other'),
    ]
    series = forms.MultipleChoiceField(
        choices = SERIES_CHOICES,
        required = False,
        label = 'Series',
        widget = forms.CheckboxSelectMultiple
    )

    SCARLET_VIOLET_SETS = [
        ('sv8', 'Surging Sparks'),
        ('sv7', 'Stellar Crown'),
        ('sv6pt5', 'Shrouded Fabel'),
        ('sv6', 'Twilight Masquerade'),
        ('sv5', 'Temporal Forces'),
        ('sv4pt5', 'Paldean Fates'),
        ('sv4', 'Paradox Rift'),
        ('sv3pt5', '151'),
        ('sv3', 'Obsidian Flames'),
        ('sv2', 'Paldea Evolved'),
        ('sv1', 'Scarlet & Violet Base'),
        ('sve', 'Scarlet & Violet Energies'),
        ('svp', 'SV Black Star Promos'),
    ]
    scarlet_violet_sets = forms.MultipleChoiceField(
        choices = SCARLET_VIOLET_SETS,
        required = False,
        label = 'Scarlet Violet',
        widget = forms.CheckboxSelectMultiple
    )

    # Pokémon Subtypes
    POKEMON_CHOICES = [
        ('Ancient', 'Ancient'),
        ('BREAK', 'BREAK'),
        ('Baby', 'Baby'),
        ('Basic', 'Basic'),
        ('EX', 'EX'),
        ('Eternamax', 'Eternamax'),
        ('Fusion Strike', 'Fusion Strike'),
        ('Future', 'Future'),
        ('GX', 'GX'),
        ('LEGEND', 'LEGEND'),
        ('Level-Up', 'Level-Up'),
        ('MEGA', 'MEGA'),
        ('Prime', 'Prime'),
        ('Prism Star', 'Prism Star'),
        ('Radiant', 'Radiant'),
        ('Rapid Strike', 'Rapid Strike'),
        ('Restored', 'Restored'),
        ('SP', 'SP'),
        ('Single Strike', 'Single Strike'),
        ('Stage 1', 'Stage 1'),
        ('Stage 2', 'Stage 2'),
        ('Star', 'Star'),
        ('TAG TEAM', 'TAG TEAM'),
        ('Team Plasma', 'Team Plasma'),
        ('Tera', 'Tera'),
        ('Ultra Beast', 'Ultra Beast'),
        ('V', 'V'),
        ('V-UNION', 'V-UNION'),
        ('VMAX', 'VMAX'),
        ('VSTAR', 'VSTAR'),
    ]
    pokemon_subtypes = forms.MultipleChoiceField(
        choices=POKEMON_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Pokémon Subtypes"
    )

    # Trainer Subtypes
    TRAINER_CHOICES = [
        ('ACE SPEC', 'ACE SPEC'),
        ('Ancient', 'Ancient'),
        ('Fusion Strike', 'Fusion Strike'),
        ('Future', 'Future'),
        ('Goldenrod Game Corner', 'Goldenrod Game Corner'),
        ('Item', 'Item'),
        ('Pokemon Tool', 'Pokemon Tool'),
        ('Pokemon Tool F', 'Pokemon Tool F'),
        ('Rapid Strike', 'Rapid Strike'),
        ('Rocket’s Secret Machine', 'Rocket’s Secret Machine'),
        ('Single Strike', 'Single Strike'),
        ('Stadium', 'Stadium'),
        ('Star', 'Star'),
        ('Supporter', 'Supporter'),
        ('TAG TEAM', 'TAG TEAM'),
        ('Team Plasma', 'Team Plasma'),
        ('Technical Machine', 'Technical Machine'),
    ]
    trainer_subtypes = forms.MultipleChoiceField(
        choices=TRAINER_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Trainer Subtypes"
    )

    # Energy Subtypes
    ENERGY_CHOICES = [
        ('ACE SPEC', 'ACE SPEC'),
        ('Basic', 'Basic'),
        ('Fusion Strike', 'Fusion Strike'),
        ('Rapid Strike', 'Rapid Strike'),
        ('Single Strike', 'Single Strike'),
        ('Special', 'Special'),
        ('Star', 'Star'),
        ('Team Plasma', 'Team Plasma'),
    ]
    energy_subtypes = forms.MultipleChoiceField(
        choices=ENERGY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Energy Subtypes"
    )

    combine_subtypes = forms.ChoiceField(
        choices=[('and', 'Match All (AND)'), ('or', 'Match Any (OR)')],
        widget=forms.RadioSelect,
        required=False,
        initial='or'
    )

    TYPES = [
        ('colorless', 'Colorless'),
        ('darkness', 'Darkness'),
        ('dragon', 'Dragon'),
        ('fairy', 'Fairy'),
        ('fighting', 'Fighting'),
        ('fire', 'Fire'),
        ('grass', 'Grass'),
        ('lightning', 'Lightning'),
        ('metal', 'Metal'),
        ('psychic', 'Psychic'),
        ('water', 'Water'),
    ]
    types = forms.MultipleChoiceField(
        choices = TYPES,
        widget = forms.CheckboxSelectMultiple,
        required=False,
        label="Types"
    )

    COMMON_RARITIES = [
        ('', 'Choose a Rarity'),
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('rare holo', 'Rare Holo'),
        ('double rare', 'Double Rare'),
        ('ace spec rare', 'ACE SPEC Rare'),
        ('illustration rare', 'Illustration Rare'),
        ('ultra rare', 'Ultra Rare'),
        ('shiny rare', 'Shiny Rare'),
        ('shiny ultra rare', 'Shiny ultra Rare'),
        ('rare shiny', 'Rare Shiny'),
        ('rare secret', 'Rare Secret'),
        ('special illustration rare', 'Special Illustration Rare'),
        ('hyper rare', 'Hyper Rare'),
        ('rare rainbow', 'Rare Rainbow'),
        ('radiant rare', 'Radiant Rare'),
        ('amazing rare', 'Amazing Rare'),
        ('trainer gallery rare holo', 'Trainer Gallery Rare Holo'),
        ('promo', 'Promo'),
    ]
    common_rarities = forms.ChoiceField(
        choices=COMMON_RARITIES,
        required=False,
        label="Common Rarities"
    )

    OTHER_RARITIES = [
        ('', 'Choose a Rarity'),
        ('classic collection', 'Classic Collection'),
        ('legend', 'LEGEND'),
        ('rare ace', 'Rare ACE'),
        ('rare break', 'Rare BREAK'),
        ('rare prime', 'Rare Prime'),
        ('rare prism star', 'Rare Prism Star'),
        ('rare shining', 'Rare Shining'),
        ('rare shiny gx', 'Rare Shiny GX'),
        ('rare ultra', 'Rare Ultra'),
        ('rare holo ex', 'Rare Holo Ex'),
        ('rare holo gx', 'Rare Holo GX'),
        ('rare holo lv.x', 'Rare Holo LV.X'),
        ('rare holo star', 'Rare Holo Star'),
        ('rare holo v', 'Rare Holo V'),
        ('rare holo vmax', 'Rare Holo VMAX'),
        ('rare holo vstar', 'Rare Holo VSTAR'),
    ]
    other_rarities = forms.ChoiceField(
        choices=OTHER_RARITIES,
        required=False,
        label="Other Rarities"
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'list':'dataListOptions',
                   'placeholder': 'Search for a card'
            }),
        label="Name",
        max_length=100,
        required=False)
