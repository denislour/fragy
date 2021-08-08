def configs(app, settings_override):
    """
        Config app (mutates the app passing in).

        :params: Flask app instance
        :return: None
    """
    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if settings_override is not None:
        app.config.update(settings_override)
