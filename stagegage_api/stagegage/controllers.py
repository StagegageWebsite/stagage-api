"""
Manage calls to database
"""

from .models import *
from django.db.models import *



def top_genres(artist):
    """
    Return the top 3 genres for an artist
    :return: ['abc', 'abc', 'abc']
    """
    return Genre.objects.filter(artist=artist)\
               .values_list("genre", flat=True)\
               .annotate(votes=Count("genre"))\
               .order_by('-votes')[:3]
