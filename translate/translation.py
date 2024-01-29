from modeltranslation.translator import TranslationOptions, translator

from translate.models import Person


class PersonTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name',)


translator.register(Person, PersonTranslationOptions)
