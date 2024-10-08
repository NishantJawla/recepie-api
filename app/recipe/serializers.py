"""
Serializers for recipe app
"""

from rest_framework import serializers

from core.models import (
    Recipe,
    Tag,
)

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']

class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for Recipe objects
    """

    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [ 'id', 'title', 'time_minutes', 'price', 'link', 'tags']
        read_only_fields = ['id']

    def _get_or_create_tags(self, tags, recipe):
        """Handle getting or creating tags as needed."""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, _created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tags.add(tag_obj)
    
    def create(self, validated_data):
        """Create a recipe."""
        tags = validated_data.pop('tags', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)

        return recipe
    
    def update(self, instance, validated_data):
        """Update a recipe."""
        tags = validated_data.pop('tags', [])
        recipe = super().update(instance, validated_data)
        recipe.tags.clear()
        self._get_or_create_tags(tags, recipe)

        return recipe

class RecipeDetailSerializer(RecipeSerializer):
    """
    Serializer for Recipe detail objects
    """

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
