from djongo import models


class Article(models.Model):
    # _id = models.BigAutoField()
    # slug = models.TextField(max_length=255, unique=True)
    title = models.CharField(max_length=255)

    # description = models.TextField()
    body = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


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
        null=True,
        blank=True,
    )
    content = models.TextField()
    authors = models.ArrayReferenceField(
        to=Author,
        on_delete=models.CASCADE,
        related_name='article_entry',
        null=True
    )

    def __str__(self):
        return self.content


class Tag(models.Model):
    tag = models.CharField(max_length=255)
    slug = models.TextField(db_index=True, unique=True)

# class Company(models.Model):
#     name = models.CharField(max_length=255)
