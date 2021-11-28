from django.contrib import admin

from .models import profissionalenc_profissionalenc
from .models import paciente_paciente
from .models import avaliacaoad_avaliacaoad
from .models import comunicoral_comunicoral
from .models import comunicoralidade_comunicoralidade
from .models import TipoVoz
from .models import Ressonancia
from .models import AtaqueVocal
from .models import Pitch
from .models import Loudness
from .models import Modulacao
from .models import Qualidadeemis
from .models import TipoVozCad
from .models import RessonanciaCad
from .models import AtaqueVocalCad
from .models import PitchCad
from .models import LoudnessCad
from .models import ModulacaoCad
from .models import QualidadeemisCad

admin.site.register(profissionalenc_profissionalenc)
admin.site.register(paciente_paciente)
admin.site.register(avaliacaoad_avaliacaoad)
admin.site.register(comunicoral_comunicoral)
admin.site.register(comunicoralidade_comunicoralidade)
admin.site.register(TipoVoz)
admin.site.register(Ressonancia)
admin.site.register(AtaqueVocal)
admin.site.register(Pitch)
admin.site.register(Loudness)
admin.site.register(Modulacao)
admin.site.register(Qualidadeemis)
admin.site.register(TipoVozCad)
admin.site.register(RessonanciaCad)
admin.site.register(AtaqueVocalCad)
admin.site.register(PitchCad)
admin.site.register(LoudnessCad)
admin.site.register(ModulacaoCad)
admin.site.register(QualidadeemisCad)
