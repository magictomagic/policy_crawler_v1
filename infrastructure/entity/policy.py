import snowflake.client
from tortoise import Model, fields
from snowflake import SnowflakeGenerator
import jellyfish


class NewsAbstract(Model):
    news_abstract_id = fields.IntField(pk=True)
    abstract_entrance = fields.CharField(max_length=250)
    href = fields.CharField(max_length=250, null=True)
    title = fields.CharField(max_length=250, null=True)
    assert_time = fields.CharField(max_length=50, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)

    def __eq__(self, other):
        if not isinstance(other, NewsAbstract):
            return NotImplemented
        if hash(self) != hash(other):
            return False
        return self.abstract_entrance == other.abstract_entrance and self.href == other.href

    def __hash__(self):
        return hash((self.abstract_entrance, self.href))


class NewsDetail(Model):
    news_detail_id = fields.IntField(pk=True)
    href = fields.CharField(max_length=250)
    title = fields.CharField(max_length=250, null=True)
    content = fields.CharField(max_length=100000, null=True)
    # class Meta:
    #     generate_pk = False
