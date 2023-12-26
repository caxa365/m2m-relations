from django.contrib import admin

from .models import Article, Tag, Scope
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

class ArticleFormSet(BaseInlineFormSet):
    ''' Проверка на наличие и правильное количество основных тегов'''

    def clean(self):
        count = 0
        for form in self.forms:
            is_main = form.cleaned_data['is_main']
            print(is_main)
            if is_main == True:
                count +=1  
            if count > 1:
                raise ValidationError ('Основным может быть только один раздел')
            if count == 0:
                raise ValidationError('Укажите основной раздел')
                
        return super().clean()




class ScopeAdmin(admin.TabularInline):
    model = Scope
    formset = ArticleFormSet
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeAdmin]

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass