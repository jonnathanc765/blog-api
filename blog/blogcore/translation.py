
from modeltranslation.translator import register, TranslationOptions
from .models import Category

@register(Category)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'description',)

