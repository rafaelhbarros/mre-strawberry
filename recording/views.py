# Create your views here.
import asyncio
import datetime
from typing import Optional

import strawberry
from strawberry.types import Info

from strawberry.django.views import AsyncGraphQLView
from strawberry.tools import create_type

from recording import models


@strawberry.input()
class SetRecordingInput:
    _record_id: strawberry.ID = strawberry.field()


@strawberry.type()
class RecordingInfoPayload:
    _streaming_url: strawberry.Private[Optional[str]] = None
    _expiration_time: strawberry.Private[Optional[str]] = None
    _is_expired: strawberry.Private[bool] = False
    _is_error: strawberry.Private[bool] = False
    _record: strawberry.Private[models.Recording]

    @strawberry.field(description="Twilio streaming url of the ")
    def recording_streaming_url(self) -> Optional[str]:
        return self._streaming_url

    @strawberry.field()
    def expiration_date(self) -> Optional[str]:
        expiration_time = self._expiration_time
        if expiration_time is not None:
            return str(expiration_time)
        return None

    @strawberry.field()
    def is_expired(self) -> bool:
        return self._is_expired

    @strawberry.field()
    async def is_error(self) -> bool:
        return self._is_error


async def streaming_thing_that_works_ok(uuid):
    await asyncio.sleep(0.1)
    return f"http://company.com/recording/{uuid}"


async def async_create_recording_streaming_info(
    input: SetRecordingInput, info: Info
) -> Optional[RecordingInfoPayload]:
    _record: models.Record = await models.Recording.objects.filter(uuid=input._record_id).afirst()

    if _record is None:
        raise Exception("Custom exception: record is None")

    # build streaming url with internal service
    streaming_url = streaming_thing_that_works_ok(_record.uuid)
    _is_expired = False
    _is_error = False


    return RecordingInfoPayload(
        _streaming_url = streaming_url,
        _expiration_time = datetime.datetime.now() + datetime.timedelta(hours=1),
        _is_expired = _is_expired,
        _is_error = _is_error,
        _record = _record
    )
    

async_create__recording_streaming_info_mutation = strawberry.field(
    name="createRecordingStreamingInfo",
    resolver=async_create_recording_streaming_info,
    description="",
)  # type: ignore


Mutation = create_type(
    "Mutation",
    [async_create__recording_streaming_info_mutation]
)

schema = strawberry.federation.Schema(
    query=None,
    mutation=Mutation,
    types=[],  # type: ignore
    extensions=[],
)


mre_view = AsyncGraphQLView.as_view(graphiql=True, schema=schema)