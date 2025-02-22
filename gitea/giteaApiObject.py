from .basicGiteaApiObject import BasicGiteaApiObject


class GiteaApiObject(BasicGiteaApiObject):
    GET_API_OBJECT = "FORMAT/STRING/{argument}"
    PATCH_API_OBJECT = "FORMAT/STRING/{argument}"

    def __init__(self, gitea):
        super(GiteaApiObject, self).__init__(gitea)

    @classmethod
    def request(cls, gitea, id):
        """Use for giving a nice e.g. 'request(gita, orgname, repo, ticket)'.
        All args are put into an args tuple for passing around"""
        return cls._request(gitea)

    @classmethod
    def _request(cls, gitea, args):
        result = cls._get_gitea_api_object(gitea, args)
        api_object = cls.parse_response(gitea, result)
        # hack: not all necessary request args in api result (e.g. repo name in issue)
        for key, value in args.items():
            if not hasattr(api_object, key):
                setattr(api_object, key, value)
        return api_object


