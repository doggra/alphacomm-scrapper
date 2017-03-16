# -*- coding: utf-8 -*-

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import signals
from scrapy.utils.project import get_project_settings
class B2BsoftPipeline(object):
    def process_item(self, item, spider):
        return item


class ImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        settings = get_project_settings()
        image_paths = ["{}/{}".format(settings.get('IMAGES_STORE', 'images'), x['path']) for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item