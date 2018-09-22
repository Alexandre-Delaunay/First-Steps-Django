from django.http import Http404

class Article():
    lstArticle = [
        {'id': '1', 'title': 'First Article', 'body': 'This is my first Article'},
        {'id': '2', 'title': 'Second Article', 'body': 'This is my second Article'},
        {'id': '3', 'title': 'Third Article', 'body': 'This is my third Article'},
    ]

    @classmethod
    def all(cls):
        return cls.lstArticle
    
    @classmethod
    def findById(cls, id):
        try:
            return cls.lstArticle[int(id)-1]
        except:
            raise Http404('Sorry, article #{} not found'.format(id))