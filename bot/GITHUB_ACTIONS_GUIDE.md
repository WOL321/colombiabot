# 🚀 Guía Completa: GitHub Actions (100% GRATIS)

## ¿Por qué GitHub Actions?

✅ **100% GRATIS** — Sin tarjeta de crédito  
✅ **2000 minutos/mes** — Más que suficiente para tu bot  
✅ **Sin configuración compleja** — Solo sube archivos a GitHub  
✅ **Automático** — Corre cada 20 minutos  
✅ **Natural** — El bot decide aleatoriamente si enviar (simula 25-40 min)  

---

## 📋 Paso a Paso Completo

### Paso 1: Crear Cuenta en GitHub

1. Ve a [github.com](https://github.com)
2. Haz clic en **"Sign up"**
3. Crea tu cuenta (email + password)
4. Verifica tu email

### Paso 2: Crear un Repositorio

1. En GitHub, haz clic en el botón **"+"** (arriba a la derecha) → **"New repository"**
2. Configura así:
   - **Repository name:** `colombia-pride-bot`
   - **Description:** `🇨🇴 Colombia Pride Discord Bot`
   - **Public** (o Private si prefieres)
   - ✅ **"Add a README file"**
3. Haz clic en **"Create repository"**

### Paso 3: Subir los Archivos del Bot

**Opción A: Subir desde la web (más fácil)**

1. En tu repositorio, haz clic en **"Add file"** → **"Upload files"**
2. Arrastra todos los archivos de tu carpeta `bot/` aquí:
   - `bot.py`
   - `bot_github.py`
   - `config.py`
   - `requirements.txt`
   - `.github/workflows/keep-alive.yml`
   - `README.md`
   - `LICENSE`
   - `.gitignore`
   - `.env.example`
3. Haz clic en **"Commit changes"**

**Opción B: Usar Git (si sabes usar terminal)**

```bash
cd tu-carpeta-bot
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/colombia-pride-bot.git
git push -u origin main
```

### Paso 4: Configurar los Secrets (MUY IMPORTANTE)

Los secrets son donde guardas tu token y channel ID de forma segura.

1. En tu repositorio de GitHub, ve a **"Settings"** (pestaña arriba)
2. En el menú lateral izquierdo, busca **"Secrets and variables"** → **"Actions"**
3. Haz clic en **"New repository secret"**

**Añadir el Token:**
- **Name:** `DISCORD_BOT_TOKEN`
- **Secret:** (pega tu token de bot aquí)
- Haz clic en **"Add secret"**

**Añadir el Channel ID:**
- Haz clic en **"New repository secret"** otra vez
- **Name:** `DISCORD_CHANNEL_ID`
- **Secret:** (pega tu channel ID aquí)
- Haz clic en **"Add secret"**

### Paso 5: Verificar el Workflow

1. En tu repositorio, ve a la pestaña **"Actions"**
2. Deberías ver **"Colombia Pride Bot"** en la lista
3. Haz clic en él
4. Verás el workflow configurado para correr cada 20 minutos

### Paso 6: Probar Manualmente (Opcional)

Para probar que funciona sin esperar 20 minutos:

1. En la pestaña **"Actions"**, haz clic en **"Colombia Pride Bot"**
2. A la derecha, haz clic en **"Run workflow"** → **"Run workflow"**
3. Espera 1-2 minutos
4. Refresca la página — deberías ver el run completado
5. Ve a tu servidor de Discord — ¡el bot debería haber enviado un mensaje!

### Paso 7: Verificar que Funciona

1. Ve a tu servidor de Discord
2. El bot debería estar online (aunque solo corre brevemente)
3. Espera 20-40 minutos
4. Deberías ver un mensaje con embed bonito y reacciones emoji 🇨🇴

---

## 🎯 ¿Cómo Funciona?

### El Flujo:

```
Cada 20 minutos → GitHub ejecuta tu código
                ↓
        El bot decide aleatoriamente:
        - 60% → Envía un mensaje con reacciones
        - 40% → No hace nada (simula timing natural)
                ↓
        El bot se desconecta
                ↓
        Espera 20 minutos para la próxima ejecución
```

### ¿Por qué es natural?

- Se ejecuta cada 20 minutos
- Pero solo envía mensaje el 60% de las veces
- Esto crea gaps de 20-60 minutos entre mensajes
- ¡Parece completamente orgánico!

---

## 📊 Límites de GitHub Actions (Plan Gratuito)

| Límite | Valor | ¿Suficiente? |
|--------|-------|--------------|
| Minutos/mes | 2000 | ✅ Sí (usamos ~1000) |
| Almacenamiento | 500 MB | ✅ Sí (usamos ~5 MB) |
| Ejecuciones simultáneas | 20 | ✅ Sí (usamos 1) |

**Cálculo de uso mensual:**
- 3 ejecuciones/hora × 24 horas × 30 días = 2,160 ejecuciones
- Cada ejecución dura ~30 segundos
- Total: ~1,080 minutos/mes ✅

---

## 🛠️ Comandos Útiles

### Ver Logs del Bot

1. Ve a la pestaña **"Actions"** en tu repositorio
2. Haz clic en el workflow run que quieres ver
3. Haz clic en **"run-bot"**
4. Verás todos los logs

### Forzar una Ejecución Manual

1. Ve a **"Actions"** → **"Colombia Pride Bot"**
2. Haz clic en **"Run workflow"**
3. El bot enviará un mensaje inmediatamente

### Desactivar el Bot Temporalmente

1. Ve a **"Settings"** → **"Actions"** → **"General"**
2. Desmarca **"Enable Actions"**
3. El bot dejará de ejecutarse

### Actualizar el Código

1. Edita los archivos en GitHub (haz clic en el archivo → lápiz)
2. O sube nuevos archivos
3. Los cambios se aplican automáticamente en la próxima ejecución

---

## 🎉 ¡Listo!

Tu bot ahora corre **24/7 completamente gratis** en GitHub Actions.

**Características:**
- ✅ Envía mensajes cada 20-60 minutos (timing natural)
- ✅ Detecta holidays colombianos
- ✅ Añade reacciones emoji automáticamente
- ✅ 24+ variaciones de emoji
- ✅ Embeds bonitos con colores de la bandera

---

## 🆘 Troubleshooting

### El bot no envía mensajes

1. Verifica que los secrets estén configurados correctamente
2. Ve a **"Actions"** y revisa los logs
3. Asegúrate de que el bot tenga permisos en el canal

### "Workflow disabled" error

1. Ve a **"Actions"** → **"Colombia Pride Bot"**
2. Haz clic en **"Enable workflow"**

### El bot se ejecuta pero no envía nada

- Esto es normal el 40% de las veces (timing natural)
- Espera a la próxima ejecución

### Quiero cambiar la frecuencia

Edita `.github/workflows/keep-alive.yml`:

```yaml
# Cada 15 minutos (más frecuente)
- cron: '*/15 * * * *'

# Cada 30 minutos (menos frecuente)
- cron: '*/30 * * * *'
```

### Quiero cambiar la probabilidad de enviar

Edita `bot_github.py`:

```python
# 80% de probabilidad (más mensajes)
should_send = random.random() < 0.80

# 40% de probabilidad (menos mensajes)
should_send = random.random() < 0.40
```

---

## 🇨🇴 ¡Viva Colombia!

Tu bot está celebrando Colombia 24/7, completamente gratis. 🎉
