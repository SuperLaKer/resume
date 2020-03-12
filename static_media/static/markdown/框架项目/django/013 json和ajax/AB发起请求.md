```python
def prov(request):
    areas = AreaInfo.objects.filter(parent__isnull=True)

    return JsonResponse({'data': areas})
```

```javascript
$.post('/prov', {'num': 1}, function (data) {             
})
```

