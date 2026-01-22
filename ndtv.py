import requests
import functions

domain = "https://www.ndtv.com"

# The whole get request for Posts as seen on Burp Suite
post_get_req = """
GET /world-news/first-russia-us-ukraine-trilateral-to-be-held-in-uae-on-friday-volodymyr-zelensky-10836133?pfrom=home-ndtv_topscroll_Imagetopscroll HTTP/2
Host: www.ndtv.com
Cookie: compass_uid=068782ad-32b3-4268-849a-247d29e3c20d; _gcl_au=1.1.1970051442.1768980464; _sharedID=7155cedf-0c09-4985-8216-f6b1841caff4; _cb=EUqkeDoS731CJ5KiP; PublisherProvidedIdsNew=publisherprovidedids641737226ndtvids; _cc_id=c51126065c29bac181e1f43401e7a621; _vdo_ai_uuid=ed68565f-0bef-4bd7-84ab-8fccc0a6f5a1; uid-s=13fc54f-4c65-43fe-9bc7-a36521e9e7f3; vuukle_geo_region={%22country_code%22:%22IN%22%2C%22region%22:%22Uttarakhand%22%2C%22os%22:%22Windows%22%2C%22device%22:%22Desktop%22%2C%22browser%22:%22Chrome%22}; vsid=a5fe6204-2cdc-4c39-9407-afff96228257; _pubcid=06c12106-7fc3-4146-a879-19bcfa013507; __utma=165355488.298846644.1768980465.1768999884.1768999884.1; __utmc=165355488; __utmz=165355488.1768999884.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); connectId={"ttl":86400000,"lastUsed":1769002528077,"lastSynced":1769002528077}; _sharedID_cst=zix7LPQsHA%3D%3D; bm_ss=ab8e18ef4e; ak_bmsc=A62B31382490EFAA19AFCFBD2EF92A80~000000000000000000000000000000~YAAQjQFAF3RnGMebAQAA7UCq5h6VBFnJw6LmC/ifET/yVXrwBOMxuZfSJfgv8eyRMrIqqJJBSz2otOMLwHLPuaQ1f27hjmD7elFAf4I4pJZG6RVoCrplvbHHfZCe6IQlZvwh1HZQk3YrOAO07Tz0d0VhxNdDPJlAclFsKbrZ5IfqWRayQKcYEBMjO6HjoW0KtNReyx4bE9ZMGUf5ZaYfJilE/ZQhj6qz5jLxCA6r0dg/a6YBLFUKkgTp6FNLX++EPGPy69zcTQ9BH6vWdYM24Ok3L2rRVaklq/a7kdkqDHXyUa3IBW/ph1CLf15B0nbOHYSY7ylY/+57R1aqrI50MXz/HktSfvohCsarsBsZfwc/CGBAtyvPj3jVDUyXy/M8UckVTHbL/aWICA==; pbjs-unifiedid=%7B%22TDID%22%3A%22f4a856a8-f02c-4980-ac4f-ee18995a5069%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222025-12-22T17%3A04%3A43%22%7D; pbjs-unifiedid_cst=zix7LPQsHA%3D%3D; panoramaId_expiry=1769187898403; panoramaId=6a56b9d323aa5adfa62c53907d5da9fb927ae618ac860a85369892fd3118edb8; panoramaIdType=panoDevice; _cb_svref=https%3A%2F%2Fwww.google.com%2F; ___nrbi=2|t97e24|068782ad-32b3-4268-849a-247d29e3c20d|%5B%5D|t99zgf|9|||; _ga_EDK4P8CHKM=GS2.1.s1769101504$o3$g0$t1769101504$j60$l0$h0; cto_bundle=uOZHgV9vJTJCOE45eUFIUlhvT0J0Y2VERDhyclQ3NlJSTU8lMkJNb3M3eFRsZWJUR093Z1c2RG5oZG5NN1M2c21EZ2F3OE9SaHVNbGJqVHQlMkJmM1BtazdrUjFCYVJwSUQ4ZldXYkNMdHo5UVVxT2tkWFdlZkg0N0VSUGE3OW10MFluNk9EWGZuRnlnSVg4MW1YdDJ4UFFCdEhaSDJyN2clM0QlM0Q; _clck=10szmxu%5E2%5Eg2x%5E0%5E2212; tvc_adBlocker_check=0; _SUPERFLY_lockout=1; __gads=ID=c8ac6c5a2fce9242:T=1768980468:RT=1769101826:S=ALNI_MZrqVv5h3ywChhYYp7bzZIq7_MOfQ; __gpi=UID=000011e91c18a6b2:T=1768980468:RT=1769101826:S=ALNI_Mbv_GorwHOLYACV2ljRPxlGio-RhQ; __eoi=ID=152f21b3a65cdba6:T=1768980468:RT=1769101826:S=AA-AfjZrCfwIlj6zRvyFc99Oa54S; _gid=GA1.2.1990011793.1769101854; _clsk=vd77aw%5E1769101864073%5E1%5E0%5Ei.clarity.ms%2Fcollect; bm_so=279FD810431C8F2BC3535D82BFED48B8EE1448BFACC537DE140FF37BC01242BB~YAAQjQFAF0/3GMebAQAAdvuw5gb/atvsd7CB/jzpzD6f9RtndD0NHaNXrN+qPur25HaZvIRBKRBiJWoJ8Q9hjWgjxhF/NM60HTUNO7SPXngJiWnXFzg3dKKLmPyhZej4LDqkNQP7/FY51gZ2+v7vhDxw2hcoPIWZkYwzYzVhXGUX5l9suO1FLaiboj62i3JtR5rox0CXWcxwFHUK1VZtdKURc5bKgkLHdB59x+2Wxgl664wHEnt++PdNgvG1x1G31cdh307iIj7Mz6Pfr5i0qOyw0li56zMdbxVUpfZWleT946BTp6rRnWr8u2RpP0XVUblvA2FnGe0/cwMoe6xnwZ2G+cp3sAJIILbDHJvEd1B4DTRy0+RGR33iPw+fjKIygTEbiSzacvqq/Ng5GQ8gg1gciCE/NszQ24syOLc+Rs/XK1D2EI+G/Hl58Rg1l8fmaLEfJ60Y6lFr8J1w; _chartbeat4=t=CuDCJ6DIjaEXD0-8LoCq3e6xQJVTs&E=65&x=0&c=6.91&y=11548&w=598; _ga_WHYDFTB5HJ=GS2.1.s1769101480$o4$g1$t1769101918$j60$l0$h0; _chartbeat2=.1768980464809.1769101918704.11.CPK6mjDcIXwjC6qoqJC0uUufDNhqQC.3; ___nrbic=2|t99zry|t97vcg|t99zgf|23ed8cf8-9fa5-4ced-9522-973018741d91|%5B%5D|true|3|https%3A%2F%2Fwww.ndtv.com%2F|https%3A%2F%2Fwww.google.com%2F||; bm_sv=A037AF24E8070CC7A595F437EBE720D0~YAAQTWw/F4sE89ebAQAA7QCx5h5QfcKftf/35rSaK+a2Ki8Tubv5UYASy5mqu1TRFhno2S8ldlNgnbZAB1yAkoKRH8g/B4IqzSISTF2Z7PykIeYLLBlSJjWisdP9xNZoYfr6177QzHMg1CvAdInE7iH2YIPkgjFYRAve3wX8IhVOgb88JvCbBoQjzaDz4oulcxjfyHJpQyJBfu7cUl9LK0HziXBGXpcN8ATsYMpnzrRkXj8Z350LgakldFvQAUI=~1; _gat_gtag_UA_113932176_46=1; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22df36341f-1d8a-4dfd-96f5-50ac2b45ddac%5C%22%2C%5B1768980468%2C518000000%5D%5D%22%5D%5D%5D; _ga_8J9SC9WB3T=GS2.1.s1769101853$o5$g1$t1769101920$j59$l0$h0; _ga_HXEC5QES15=GS2.1.s1769101855$o4$g1$t1769101921$j1$l0$h0; _ga=GA1.1.298846644.1768980465; bm_s=YAAQjQFAF5j4GMebAQAABgmx5gRbtO8pm2sGcuTFfVSHZqHs/hzat2sXMvqWZ/DBTD6WhHLNcrvwbg3D9BRxm6osZrf1loCiiBa5xFlIjC+UZS0gx0snp0nFTCOu4MIogMFCQrGkOAaJ16MX16YDKSPUSi+9Zx8keQpuj6y4K1VqqnsKaGY9A0SQx7tWg++YudS18sfHVLkv3LyHzqSmS1kuny5m0zC9l3gwJyD0O1+cvu7HdVU3E4jo5+PjCTPnBy9oftRMZweyRjZUY7Afk17WfgaGCzxOJ1yFFeguwGYrCEn9AsF6Y/PvdoyrwBIDUVNIOUDlDBNp/KUihra+OnzzN5qQtwXwmQaj0Yyl0dvl/yDeCk6wU/6yObYG8/wvw9C6tsv9WB9//g8Ied4glUTcT9kaA7Ao+N4LoqLqFej8M9KvMuHBLPWWCfTZoVyorlUGtSgCuxzirBf346V9hHq8LyGndedR4rqqqzjIWvQJ9FEIU3KCf9sLACfoLRFnVZ0EQ4z7G3UErMYJvjHSuusoHmqTy4ikOCEhe3o8YrcUhrrBOq+6VU0O4Q==; _awl=2.1769101920.5-abe6086c45c8df7e24f088df8b369213-6763652d617369612d6561737431-0; _ga_M7E3P87KRC=GS2.1.s1769101500$o4$g1$t1769101921$j1$l0$h608451548; FCNEC=%5B%5B%22AKsRol_4tSFBDPv2qU_GlN8khxFzWm2Tz6B2knFdsfrnaKD8EWCjD2_dVcNvfL4fjFURDNPscVR-NB5Wrw_OPX6pkj2Y2Tw0uemvsgwPQlafBgRDCymeUhCDjzkTCS395jpf-S86zhakIWC_o08J7sWSVQcFzdmIew%3D%3D%22%5D%5D; _pubcid_cst=znv0HA%3D%3D; __insagBGPercentage=25; __binsSID=4a60d789-f4f7-4470-b4c1-4447f0809c2e; __binsUID=075c2d19-c3d8-432a-8823-9eaadcab3259; _ga_XQCGTLW8NV=GS2.1.s1769101479$o4$g1$t1769101927$j54$l0$h397955276; g_state={"i_l":0,"i_ll":1769101954214,"i_b":"KTGemWbscWwDcLJ59JF6Mh62sjn95eh3W9EPZdT3pKk","i_e":{"enable_itp_optimization":3}}; bm_lso=279FD810431C8F2BC3535D82BFED48B8EE1448BFACC537DE140FF37BC01242BB~YAAQjQFAF0/3GMebAQAAdvuw5gb/atvsd7CB/jzpzD6f9RtndD0NHaNXrN+qPur25HaZvIRBKRBiJWoJ8Q9hjWgjxhF/NM60HTUNO7SPXngJiWnXFzg3dKKLmPyhZej4LDqkNQP7/FY51gZ2+v7vhDxw2hcoPIWZkYwzYzVhXGUX5l9suO1FLaiboj62i3JtR5rox0CXWcxwFHUK1VZtdKURc5bKgkLHdB59x+2Wxgl664wHEnt++PdNgvG1x1G31cdh307iIj7Mz6Pfr5i0qOyw0li56zMdbxVUpfZWleT946BTp6rRnWr8u2RpP0XVUblvA2FnGe0/cwMoe6xnwZ2G+cp3sAJIILbDHJvEd1B4DTRy0+RGR33iPw+fjKIygTEbiSzacvqq/Ng5GQ8gg1gciCE/NszQ24syOLc+Rs/XK1D2EI+G/Hl58Rg1l8fmaLEfJ60Y6lFr8J1w~1769101955075
Cache-Control: max-age=0
Sec-Ch-Ua: "Not(A:Brand";v="8", "Chromium";v="144"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36
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
GET /2026-01/amr9g348_zelensky-afp_625x300_22_January_26.jpeg?downsize=773:435 HTTP/2
Host: c.ndtvimg.com
Cookie: ak_bmsc=45FF98C93BB2A635555CAF50D48D7358~000000000000000000000000000000~YAAQjQFAF6dnGMebAQAAYEOq5h7HAm6aMGGawPtQ5pvSo9i49tFGFp+mTUo0BhWotIOj5l76dJn+SxTDnBHfmQblav6wxPg6cSKthP16gitUvpj5+txij6WJe9oQdt6mNE3eTzQNDUcaCoD7bAPv/YjcwHJId3T1k+HJPi37RjWZVJ4V/qmdEnx2dnHF++du3iuUzW9Bk/jO9nhYFvhsDi1XRzaBoLdVCPpodtRjDUeHijQWl8uzF2hOu4HBNR1cQXe4xd7dVJvzWgG6FMafhNbrM3WRQWLN56cRSpyJLiIhlM63nvJJWJNT2t7bvQdAOR1brPw67N3hHuJy+XsSX32T5+xPUJAcEgE+JWehrha8UmbfpYTARpGwjNWU3SS5M5KtXruTVWDvAJhZ1A==
Cache-Control: max-age=0
Sec-Ch-Ua: "Not(A:Brand";v="8", "Chromium";v="144"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.ndtv.com/
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive
"""

image_headers = functions.req_to_dict(image_get_request)

img = requests.get(url= image_url, headers= image_headers)

folder_location = "D:/Veer/Web Scraper/Images/"
image_name = functions.get_image_name(image_get_request)
file_path = folder_location + image_name + ".jpeg"

open(file_path, "wb").write(img.content)