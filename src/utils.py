from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginators(request, objects, count=10):
    paginator = Paginator(objects, count)
    page = request.GET.get('page')
    try:
        mass = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mass = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        mass = paginator.page(paginator.num_pages)
    return mass


def to_list(obj, n):
    obj_count = len(obj)
    list_count = obj_count / n if not obj_count % n else (obj_count / n + 1)
    tmp = []
    for i in range(list_count):
        tmp.append(obj[i*n:(i+1)*n])
    return tmp

def translit(locallangstring):
    conversion = {
        u'\u0030' : '0',    u'\u0031' : '1',
        u'\u0032' : '2',    u'\u0033' : '3',
        u'\u0034' : '4',    u'\u0035' : '5',
        u'\u0036' : '6',    u'\u0037' : '7',
        u'\u0038' : '8',    u'\u0039' : '9',
        u'\u0410' : 'A',    u'\u0430' : 'a',
        u'\u0411' : 'B',    u'\u0431' : 'b',
        u'\u0412' : 'V',    u'\u0432' : 'v',
        u'\u0413' : 'G',    u'\u0433' : 'g',
        u'\u0414' : 'D',    u'\u0434' : 'd',
        u'\u0415' : 'E',    u'\u0435' : 'e',
        u'\u0401' : 'Yo',   u'\u0451' : 'yo',
        u'\u0416' : 'Zh',   u'\u0436' : 'zh',
        u'\u0417' : 'Z',    u'\u0437' : 'z',
        u'\u0418' : 'I',    u'\u0438' : 'i',
        u'\u0419' : 'Y',    u'\u0439' : 'y',
        u'\u041a' : 'K',    u'\u043a' : 'k',
        u'\u041b' : 'L',    u'\u043b' : 'l',
        u'\u041c' : 'M',    u'\u043c' : 'm',
        u'\u041d' : 'N',    u'\u043d' : 'n',
        u'\u041e' : 'O',    u'\u043e' : 'o',
        u'\u041f' : 'P',    u'\u043f' : 'p',
        u'\u0420' : 'R',    u'\u0440' : 'r',
        u'\u0421' : 'S',    u'\u0441' : 's',
        u'\u0422' : 'T',    u'\u0442' : 't',
        u'\u0423' : 'U',    u'\u0443' : 'u',
        u'\u0424' : 'F',    u'\u0444' : 'f',
        u'\u0425' : 'H',    u'\u0445' : 'h',
        u'\u0426' : 'Ts',   u'\u0446' : 'ts',
        u'\u0427' : 'Ch',   u'\u0447' : 'ch',
        u'\u0428' : 'Sh',   u'\u0448' : 'sh',
        u'\u0429' : 'Sch',  u'\u0449' : 'sch',
        u'\u042a' : '',    u'\u044a' : '',
        u'\u042b' : 'Y',    u'\u044b' : 'y',
        u'\u042c' : '',   u'\u044c' : '',
        u'\u042d' : 'E',    u'\u044d' : 'e',
        u'\u042e' : 'Yu',   u'\u044e' : 'yu',
        u'\u042f' : 'Ya',   u'\u044f' : 'ya',
        u'\u0020' : '_',    u'\u2116' : 'N',
        u'\u2013' : '_',    u'\u2012' : '_',
        u'\u2015' : '_',    u'\u2014' : '_',
        u'\u0040' : '_',    u'\u0022' : '_',
        u'\u0027' : '_',    u'\u0024' : '_',
        u'\u0025' : '_',    u'\u0026' : '_',
        u'\u0029' : '_',    u'\u0028' : '_',
        u'\u0021' : '_',    u'\u0023' : '_',
        u'\u002A' : '_',    u'\u002C' : '_',
        u'\u003F' : '_',    u'\u002B' : '_',
    }
    translitstring = []
    for c in locallangstring:
        translitstring.append(conversion.setdefault(c, c))
    return ''.join(translitstring)
