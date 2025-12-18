
from supabase import create_client

def inicializar_db():
    usuarios = create_client("https://sileoilsthgmspchujnm.supabase.co","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNpbGVvaWxzdGhnbXNwY2h1am5tIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwMjI0NTEsImV4cCI6MjA4MTU5ODQ1MX0.4JcisBbUFiJAtLYKC_PsL0-Ti4uCKT4XDsyi6i0prfI")
    return usuarios