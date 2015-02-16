from sharepoint import SharePointSite, basic_auth_opener

server_url = "https://mydocs.digcat.com/share"
site_url = server_url + "sites/foo/bar"

opener = basic_auth_opener(server_url, "admin", "admin")

site = SharePointSite(site_url, opener)

for sp_list in site.lists:
    print sp_list.id, sp_list.meta['Title']


print site
print opener
