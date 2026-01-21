import requests
import functions


domain = "https://www.ndtv.com"

# The whole get request for Posts as seen on Burp Suite
post_get_req = """
GET /travel/worlds-10-busiest-airline-routes-in-january-2026-mumbai-delhi-on-the-list-10799753?pfrom=home-ndtv_lateststories HTTP/2
Host: www.ndtv.com
Cookie: compass_uid=068782ad-32b3-4268-849a-247d29e3c20d; _gcl_au=1.1.1970051442.1768980464; _sharedID=7155cedf-0c09-4985-8216-f6b1841caff4; _cb=EUqkeDoS731CJ5KiP; _clck=10szmxu%5E2%5Eg2w%5E0%5E2212; PublisherProvidedIdsNew=publisherprovidedids641737226ndtvids; _cc_id=c51126065c29bac181e1f43401e7a621; panoramaId_expiry=1769066885271; panoramaId=6a56b9d323aa5adfa62c53907d5da9fb927ae618ac860a85369892fd3118edb8; panoramaIdType=panoDevice; cto_bundle=wUHOiV9vJTJCOE45eUFIUlhvT0J0Y2VERDhycmRwNGJmZGtDZ241N0RabTRINXV1dXpVUjNUJTJGZE85anRGME1CS0ZNRUMlMkYxUzZtTzUzVHpuUm9nSGxHbjNPUnI0VU1WOUxFRHAwUm8lMkIlMkZtdzFENiUyQlBGdGklMkJ1S2RHTkR5YnM3U3pHaG1FM2U5bjh2cWFXdTkzcHJUSmRYZFhLUE1ZQSUzRCUzRA; _vdo_ai_uuid=ed68565f-0bef-4bd7-84ab-8fccc0a6f5a1; uid-s=13fc54f-4c65-43fe-9bc7-a36521e9e7f3; vuukle_geo_region={%22country_code%22:%22IN%22%2C%22region%22:%22Uttarakhand%22%2C%22os%22:%22Windows%22%2C%22device%22:%22Desktop%22%2C%22browser%22:%22Chrome%22}; vsid=a5fe6204-2cdc-4c39-9407-afff96228257; _pubcid=06c12106-7fc3-4146-a879-19bcfa013507; _pubcid_cst=zix7LPQsHA%3D%3D; _gid=GA1.2.506619979.1768980562; ak_bmsc=B921446763F09CA394F80AC01512B54D~000000000000000000000000000000~YAAQhQFAF5KOltibAQAA9OKP4B4CZo6tRibAqQ2EYTWpLvPk3IEvfo855gRxxoy60HSexeR8+WsU4Rv5q1A9D9xhue6pYubfF5PARUlv68NLZMQEGoOmu07nESMSe5BUEf6TyGtRpYTCD6P5ZWhF8HIuWywZ7rGRYqJkff9oarDzILmJ1AMl7sCrEvkNeAothlrqvDnb2VFji8iM3UvIQCkGOWghB+KS+z8Fzwehv6Ip69BfVOoxT2V7mLLZ4ytgD9jcqUEedjpJnJmTZ4NdNZLvkZtuS36UCHOb6Os9JqfwnGkmEx9n94hH/Nv5yoICnXcwgI1qIkmgbGtqr71E3NL9X01lQncBDH79PzX9iUI/rejVs9wVA1S+EoAQL5hSJ/R83Qjn9/Sh; _ga=GA1.1.298846644.1768980465; _ga_HXEC5QES15=GS2.1.s1768999103$o3$g1$t1768999868$j60$l0$h0; pbjs-unifiedid=%7B%22TDID%22%3A%22f4a856a8-f02c-4980-ac4f-ee18995a5069%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222025-12-21T12%3A51%3A07%22%7D; pbjs-unifiedid_cst=kSylLAssaw%3D%3D; __utma=165355488.298846644.1768980465.1768999884.1768999884.1; __utmc=165355488; __utmz=165355488.1768999884.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _SUPERFLY_lockout=1; tvc_adBlocker_check=1; connectId={"ttl":86400000,"lastUsed":1769002528077,"lastSynced":1769002528077}; bm_ss=ab8e18ef4e; _ga_8J9SC9WB3T=GS2.1.s1769002863$o4$g0$t1769002863$j60$l0$h0; ___nrbic=2|t97vcg|t97ux7|t97sfn|ad1b3aef-6fe1-4ad9-9b7a-88b6b9835bdb|%5B%5D|true|1|https%3A%2F%2Fwww.ndtv.com%2F|https%3A%2F%2Fwww.google.com%2F||; ___nrbi=2|t97e24|068782ad-32b3-4268-849a-247d29e3c20d|%5B%5D|t97vcg|8|||; _cb_svref=https%3A%2F%2Fwww.google.com%2F; _ga_EDK4P8CHKM=GS2.1.s1768999096$o2$g1$t1769002864$j58$l0$h0; __gads=ID=c8ac6c5a2fce9242:T=1768980468:RT=1769002865:S=ALNI_MZrqVv5h3ywChhYYp7bzZIq7_MOfQ; __gpi=UID=000011e91c18a6b2:T=1768980468:RT=1769002865:S=ALNI_Mbv_GorwHOLYACV2ljRPxlGio-RhQ; __eoi=ID=152f21b3a65cdba6:T=1768980468:RT=1769002865:S=AA-AfjZrCfwIlj6zRvyFc99Oa54S; _clsk=kucrq8%5E1769002868302%5E1%5E0%5Ei.clarity.ms%2Fcollect; _chartbeat5=246|1327|%2F|https%3A%2F%2Fwww.ndtv.com%2Ftravel%2Fworlds-10-busiest-airline-routes-in-january-2026-mumbai-delhi-on-the-list-10799753%3Fpfrom%3Dhome-ndtv_lateststories|DdYijaD59pt20eswVDJOf7bBzVFO1||c|DdYijaD59pt20eswVDJOf7bBzVFO1|ndtv.com||; bm_s=YAAQDhzFF2PlNtmbAQAA57jJ4ARyfZOWLfS4NynWKAqkYpqS6GxrDWDCPCZibbHDxJjrHpY1kB6BsYhIWz8C+Iz0aV4a6nRWFoXmUwxvkycsagSQ65TcU+r6iPZwkGMfAfLpJrwtl2pCwcoviX4hVKlhCT2pkX92zejEYPwvGUAyrU4cV9jI0ewW70QPVaxMzp+bWSGuMRONNmKBp/6HoBsIlGUAaTC2gpCU1TlsNvr2M4mzgcvLlPDqFgk+FoehXiSQlxpW4ZuE187UcdZCoyNdWvgSHawvOJ/7gz/DT/NP5zajIZ7nwt7zUzpvAqkB/gpPyYZbykO6AjcuwYPOHv2eN2iMQ2EnTLILpb7aGng7JBWVugYikKwmPrLu6+a/HCeZvKF7IL/g6X1rWztmMioroUP3QYOwSlKOlaPxSxGOjDXmqBcdcJHPZJjoP89scSSAK8/f8J2ldAoNdUu8bW4IRMSrhLxdaTVYDE7vSg+VuPprTZPknh0wlcrn9SJ2tkU82flpzJEL6kj7i/0+39fYci/A8WQV8QkZTEahJUESCg6Y1JQen+QWrQ==; bm_so=D55E2E84335244C2749261D5D6ABF77F765FC8AFEF4880C97BE62BCA86812CC7~YAAQDhzFF2TlNtmbAQAA57jJ4AbEgUihh0LiPQBCQRk2nI4oHyMYKO0uAFdEoogabyp0ec7iqnocTEbZf6usil5bsyUJK7+a7FMjQYF6TUSWg9arlka5quOx2nwSr8jdrAbx82887P4rbHAs1/KlTMhoEmP9p3UFDpHkSqdHdoeDic9ceRUt9GYz5b+G6SQCDCl606QJXGlJj63TiDQQHovzzaUeyjBYj3rqI3HzfKgFbyywUutfw8UJtyjXB2bmzTvrgc6s4jQTB6OZbh5XVitpN7XwW6jeCwkiaOAnQPqwIXXIpnbGC/edUgdK44wMtOSOJNPedHYQerJUjzAuv3y2+ndDwhLBo6nTuXpex86SmyZ7WDGZc1TKH/ELo+dl73DLEg/WhnX+6aEu7LCIlWLnL5x1EkPwrH4oyAvwQOQXHpsVBgUbvifAb73a4igYe8fRoyl0k4qOfEye; _chartbeat4=t=BOJSXxBEPGkNDEa8w2j1F7hBImiJ5&E=11&x=1200&c=0.2&y=11566&w=598; _chartbeat2=.1768980464809.1769002876670.1.DJMJxSCbnqIxB0bhwm93HxRJrSZI.2; _ga_WHYDFTB5HJ=GS2.1.s1768999090$o3$g1$t1769002876$j45$l0$h0; g_state={"i_l":0,"i_ll":1769002877368,"i_b":"5NL3BzsnlASd6XM0Qudbha3H6ehWQxL9cVqt+eeg7oU","i_e":{"enable_itp_optimization":0}}; bm_lso=D55E2E84335244C2749261D5D6ABF77F765FC8AFEF4880C97BE62BCA86812CC7~YAAQDhzFF2TlNtmbAQAA57jJ4AbEgUihh0LiPQBCQRk2nI4oHyMYKO0uAFdEoogabyp0ec7iqnocTEbZf6usil5bsyUJK7+a7FMjQYF6TUSWg9arlka5quOx2nwSr8jdrAbx82887P4rbHAs1/KlTMhoEmP9p3UFDpHkSqdHdoeDic9ceRUt9GYz5b+G6SQCDCl606QJXGlJj63TiDQQHovzzaUeyjBYj3rqI3HzfKgFbyywUutfw8UJtyjXB2bmzTvrgc6s4jQTB6OZbh5XVitpN7XwW6jeCwkiaOAnQPqwIXXIpnbGC/edUgdK44wMtOSOJNPedHYQerJUjzAuv3y2+ndDwhLBo6nTuXpex86SmyZ7WDGZc1TKH/ELo+dl73DLEg/WhnX+6aEu7LCIlWLnL5x1EkPwrH4oyAvwQOQXHpsVBgUbvifAb73a4igYe8fRoyl0k4qOfEye~1769002877877; bm_sv=B5A1E0766436E73CA4EB7BEE43BE0E54~YAAQTWw/F6wpOtebAQAAV8TJ4B7Tz54wJMrDdsV7hwnCutugBb3qRy8fVtTmQc+y+gl4/Zk3ldT3P8+YnHn0JDmRm3c800iesr46rBrXYZszNodqM9y6IHQMrKOCKjuBKyk6nYvYMaHdjZtcD5GdnV2+EqtMKyfCvlkIGXLDvYWc3wTtyJGzqyi+LHX1wymUG0VatbAyJ3UtK4jWuOmEV72OQOWdNvoyNx1k0pplSAmyz9Xv48LXPw9lMf5OrqM=~1; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22df36341f-1d8a-4dfd-96f5-50ac2b45ddac%5C%22%2C%5B1768980468%2C518000000%5D%5D%22%5D%5D%5D; _awl=2.1769002879.5-abe6086c45c8df7e24f088df8b369213-6763652d617369612d6561737431-0; _ga_XQCGTLW8NV=GS2.1.s1768999090$o3$g1$t1769002880$j46$l0$h459069563; FCNEC=%5B%5B%22AKsRol-61hUFfh6TvC7Ysi4iawntakTtg6O6RlVkA6vROE1g6NT254MsR-9SJ68wmp4sbmVzu9AlzMTK4T6Z-a3OX3_ny1sdGpmJfR42sX9StsGQjUrA9iyELl8DLGMIdwEg4VIaFwkKzpRfR7YrqE_1Dkp-dV4aBA%3D%3D%22%5D%5D; _ga_M7E3P87KRC=GS2.1.s1768999097$o3$g1$t1769002882$j44$l0$h1425299699; _sharedID_cst=kSylLAssaw%3D%3D
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="143", "Not A(Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.ndtv.com/
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
"""

path = functions.get_path_from_req(post_get_req)

post_url = domain + path
# Eg: "https://www.ndtv.com" + "/travel/..."

print(post_url)

post_headers = functions.req_to_dict(post_get_req)

post_response = requests.get(url=post_url, headers=post_headers)

post_html = post_response.text

# print(html)

image_url = post_html.split('<link rel="preload" as="image" href="')[1].split('?')[0]

# print(image_url)

# The whole get request for Image as seen on Burp Suite
image_get_request = """
GET /2026-01/o4bqfvr4_busy-airport_625x300_21_January_26.jpeg HTTP/2
Host: c.ndtvimg.com
Cookie: ak_bmsc=4B8AF4C57EE468B7173419BD82B8708B~000000000000000000000000000000~YAAQhQFAF1CPltibAQAA2uOP4B7Tvzl7yj3+/vobuwG8UidW485BYxwg2a2OtDBdtN8emirBDxjf3yvcyg9WCqZsLKUEF7LCj45/qUZRR/aU9ETj1aW9i2k/c+e6mOPQ7E09L5CBuSxnWbVojLIFOAHwYI5VdP4a0YqsvMtfx07BjsVQ/wpuWHRtkGRWhZsDGCdNaWkV19tF5D73S6ILUuMbT2zmd9DiWeUsWzMQCn3UrWec/FVBB8pT/Sd7q2jOPaAeryrAnGk4unSUftwxs5R6oH6tC90QFNqF6MPsvXyGe6hh0FHw8RJgy1PNCKy3xWPSJ4dXLiFLCBOBhQsOnjburnBBqJkUXyTKoTZNuzTA/wPv+J3E0Hii5CQdvXs/5/xyBC+fLo0y2Xbf
Sec-Ch-Ua: "Chromium";v="143", "Not A(Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
"""

image_headers = functions.req_to_dict(image_get_request)

img = requests.get(url= image_url, headers= image_headers)

folder_location = "D:/Veer/Web Scraper/Images/"
image_name = functions.get_image_name(image_get_request)
file_path = folder_location + image_name + ".jpeg"

open(file_path, "wb").write(img.content)

