# Rules:
#   build
#   deploy
#   serve

import glob

python=sys.executable

rule build:
   input:
      'output/docs',
      'output/site',
      'output/mkdocs.yml',
      'output/custom'

rule deploy:
   input:
      'output/docs',
      'output/site',
      'output/mkdocs.yml',
      'output/custom'
   conda: "env/mkdocs.yml"
   shell:
      "cd output && python -m mkdocs gh-deploy"

rule serve:
   input:
      'output/docs',
      'output/site',
      'output/mkdocs.yml',
      'output/custom'
   conda: "env/mkdocs.yml"
   shell:
      "cd output && python -m mkdocs serve --no-livereload"

rule clean:
   shell:
      "find output/* | grep -v mkdocs-material-dib | xargs -n1 rm -fr"

rule process_library:
   input:
      glob.glob('library/*.md'),
      glob.glob('templates/*.md'),
      glob.glob('images/*'),
      glob.glob('stylesheets/*'),
      'templates/mkdocs.yml',
      glob.glob('scripts/*.py'),
      glob.glob('custom/*')
   output:
      directory('output/docs'),
      directory('output/custom'),
      'output/mkdocs.yml'
   conda: "env/mkdocs.yml"
   shell:
      """
#      {python} scripts/sed_fixes.py library
      {python} scripts/process.py library
      cp -r images/ output/docs/images/
      cp -r stylesheets/ output/docs/stylesheets/
      cp -r custom/ output/custom/
      """

rule mkdocs:
   input:
      'output/docs',
      'output/mkdocs.yml',
      'output/custom'
   output:
      directory('output/site')
   conda: "env/mkdocs.yml"
   shell:
      "cd output && python -m mkdocs build"
