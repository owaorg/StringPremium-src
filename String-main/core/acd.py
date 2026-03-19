async def automatic_method_search_api(api, method, request):

    if api == "depsearch":
        from core.search.api.depsearch import search_depsearch
        await search_depsearch(request)

    elif api == "infinity":
        from core.search.api.infinity import search_infinity
        await search_infinity(method, request)