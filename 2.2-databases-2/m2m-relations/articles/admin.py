from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from django.contrib import messages
from django.http import HttpRequest

from .models import Article, Scope, Tag

class RelationshipInlineFormset(BaseInlineFormSet):
    def save(self, *args, **kwargs):
        main_tag = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                main_tag += 1
        if main_tag > 1:
            raise ValidationError('Возможен только один главный тэг!')
        else:
            super().save(*args, **kwargs)


class SomeInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ordering = ['-published_at']
    inlines = [SomeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['name']




