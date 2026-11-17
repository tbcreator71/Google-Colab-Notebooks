"""Run in the existing Colab notebook namespace after the UI-assets build error."""
import uuid

if not all(name in globals() for name in ('source', 'build', 'run_step', 'os')):
    raise RuntimeError('Run this in the same Colab session where the installation cell failed.')
if not (build / 'CMakeCache.txt').is_file():
    raise RuntimeError('Existing build cache is missing; use the updated installation cell.')

RESUME_PROFILES = '562cd45a15a98eb7,060c03c81c796c6f,69ece1692368e4af'
for folder in (source / 'tools/ui/dist', build / 'tools/ui/dist'):
    if folder.exists():
        folder.rename(folder.with_name('dist-backup-' + uuid.uuid4().hex))

run_step('تهيئة المحرك بدون واجهة الويب',
         ['cmake', '-S', str(source), '-B', str(build),
          '-DLLAMA_BUILD_UI=OFF', '-DLLAMA_USE_PREBUILT_UI=OFF'], 300)
run_step('استكمال بناء المحرك الموجود',
         ['cmake', '--build', str(build), '--config', 'Release', '--target', 'llama-server',
          '-j', str(min(4, os.cpu_count() or 2))], 5400)
BINARY = build / 'bin/llama-server'
assert BINARY.is_file()
print('المحرك جاهز وقائمة الاستئناف محدثة. تابع من خلية 3 ثم 4 ثم 5؛ لا تعِد الإعدادات القديمة.')
