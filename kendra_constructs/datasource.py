import json
from constructs import Construct

from aws_cdk import aws_iam as iam, Stack, aws_kendra as kendra

default_schedule = "cron(0 0 1 * ? *)"


class KendraCrawlerV2Datasource(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        index_id,
        role_arn,
        name,
        seed_urls,
        url_inclusion_patterns,
        url_exclusion_patterns,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        self.data_source = kendra.CfnDataSource(
            self,
            "WCV2",
            index_id=index_id,
            name=name,
            type="TEMPLATE",
            data_source_configuration=kendra.CfnDataSource.DataSourceConfigurationProperty(
                template_configuration=kendra.CfnDataSource.TemplateConfigurationProperty(
                    template=json.dumps(
                        {
                            "type": "WEBCRAWLERV2",
                            "connectionConfiguration": {
                                "repositoryEndpointMetadata": {
                                    "seedUrlConnections": seed_urls
                                },
                            },
                            "repositoryConfigurations": {
                                "webPage": {"fieldMappings": []},
                                "attachment": {"fieldMappings": []},
                            },
                            "additionalProperties": {
                                "rateLimit": "300",
                                "maxFileSize": "50",
                                "crawlDepth": "10",
                                "crawlSubDomain": True,
                                "crawlAllDomain": False,
                                "maxLinksPerUrl": "100",
                                "honorRobots": True,
                            },
                            "syncMode": "FORCED_FULL_CRAWL",
                        }
                    )
                )
            ),
            role_arn=role_arn,
            schedule=default_schedule,
        )


class KendraCrawlerDatasource(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        index_id,
        role_arn,
        name,
        seed_urls,
        url_inclusion_patterns,
        url_exclusion_patterns,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        self.data_source = kendra.CfnDataSource(
            self,
            "WC",
            index_id=index_id,
            name=name,
            type="WEBCRAWLER",
            data_source_configuration=kendra.CfnDataSource.DataSourceConfigurationProperty(
                web_crawler_configuration=kendra.CfnDataSource.WebCrawlerConfigurationProperty(
                    urls=kendra.CfnDataSource.WebCrawlerUrlsProperty(
                        seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                            seed_urls=seed_urls,
                        )
                    ),
                    crawl_depth=10,
                    url_exclusion_patterns=url_exclusion_patterns,
                    url_inclusion_patterns=url_inclusion_patterns
                ),
            ),
            role_arn=role_arn,
            schedule=default_schedule,
        )
