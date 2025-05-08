import asyncio
from django.http import HttpResponse

async def async_view(request):
    for num in range(1, 10):
        await asyncio.sleep(1)
        print(num)
    return HttpResponse("Número que vai até 10.")
