from scrapy.cmdline import execute
execute(["scrapy","crawl","quotes","-o","items.json"])