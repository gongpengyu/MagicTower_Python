from source.com import items
from source.com import hero

if __name__ == "__main__":
    hero = hero.Hero()
    hero.get_item(items.ITEM_RED_MEDICINE)
    hero.get_item(items.ITEM_IRON_SWORD)
    hero.print_hero()

    hero.use_item(items.NA_RED_MED)
    hero.use_item(items.NA_IRON_SW)
    hero.print_hero()