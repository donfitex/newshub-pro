DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "phonenumber_field",
]

LOCAL_APPS = [
    "apps.core.apps.CoreConfig",
    "apps.accounts.apps.AccountsConfig",
    "apps.articles.apps.ArticlesConfig",
    "apps.categories.apps.CategoriesConfig",
    "apps.comments.apps.CommentsConfig",
    "apps.pages.apps.PagesConfig",
    "apps.newsletter.apps.NewsletterConfig",
    "apps.advertisements.apps.AdvertisementsConfig",
    "apps.analytics.apps.AnalyticsConfig",
    "apps.search.apps.SearchConfig",
    "apps.notifications.apps.NotificationsConfig",
    "apps.api.apps.ApiConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
