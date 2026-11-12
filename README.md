# Blender Colab Notebooks

Launch the notebook: [Blender GUI + Chrome Remote Desktop](https://colab.research.google.com/github/tbcreator71/Google-Colab-Notebooks/blob/Blender_Notebooks/Blender_GUI_Chrome_Remote_Desktop.ipynb)

Runs Blender in a Google Colab GPU runtime with Chrome Remote Desktop and an XFCE GUI. Designed to test Blender add-ons such as Instant Hair without a local NVIDIA GPU.

## Quick start

1. Open the notebook in Colab with a **paid runtime and positive compute units**. Connect a GPU runtime.
2. Run cells 1–3 to mount Drive, install the remote desktop and restore Blender binaries from the persistent archive cache.
3. Open https://remotedesktop.google.com/headless and obtain a fresh Linux authorization command. Run cell 4 and paste it into the hidden input along with a PIN.
4. Visit https://remotedesktop.google.com/access and connect to the Colab-Blender host.
5. In XFCE open a terminal and run `blender-colab`.
6. Optionally checkout an add-on from a public GitHub repository in cell 6. Use diagnostics if the GUI won't launch. Use cell 8 to restore or save Blender preferences.

## Persistent data

Google Drive: `MyDrive/Blender-Colab-Cache/` includes the Blender download archive, add-on Git mirrors, settings backups and a projects folder. Every new Colab VM still needs OS package installation and local extraction. **Do not leave work only in ephemeral Colab home directories.**

## Limitations

- Chrome Remote Desktop doesn't provide NVIDIA accelerated graphical OpenGL. Mesa llvmpipe software OpenGL is used as a best-effort fallback and may fail on some runtimes. CUDA GPU inference is separate from GUI rendering.
- This notebook has been syntax/structure inspected but **not executed on a live Colab GPU runtime**. Blender availability and CRD compatibility are runtime dependent.
- Do not commit authorization commands, PINs, or model access tokens. Google Colab free runtime remote-desktop limitations apply: https://research.google.com/colaboratory/faq.html
- HairDeck model weights and private Instant Hair addon code are **not bundled**. Install their dependencies through the existing project's instructions.
