from djongo import models


# Create your models here.
class Article(models.Model):
    # _id = models.BigAutoField()
    slug = models.TextField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)
    description = models.TextField()
    body = models.TextField()

    class Meta:
        abstract = True


class MetaData(models.Model):
    pub_date = models.DateField(auto_now=True)
    mod_date = models.DateField(auto_now=True)
    rating = models.IntegerField()

    class Meta:
        abstract = True


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ArticleEntry(models.Model):
    blog = models.EmbeddedField(
        model_container=Article,
    )
    meta_data = models.EmbeddedField(
        model_container=MetaData,
    )

    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()

    def __str__(self):
        return self.headline


class Tag(models.Model):
    tag = models.CharField(max_length=255)
    slug = models.TextField(db_index=True, unique=True)
