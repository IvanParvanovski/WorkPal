def has_company_permission(user, app_name, permission, company_name):
    """
    :param user: User
    :param app_name: company_profiles_app
    :param permission: add_job_offer
    :param company_name: BMW
    :return: company_profiles_app.add_job_offer_bmw
    """

    return user.has_perm(f'{app_name}.{permission}_{company_name.lower().replace(" ", "_")}')
