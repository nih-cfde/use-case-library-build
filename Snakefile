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
      'output/mkdocs.yml'

rule deploy:
   input:
      'output/docs',
      'output/site',
      'output/mkdocs.yml'
   shell:
      "cd output && {python} -m mkdocs gh-deploy"

rule serve:
   input:
      'output/docs',
      'output/site',
      'output/mkdocs.yml'
   shell:
      "cd output && {python} -m mkdocs serve --no-livereload"

rule clean:
   shell:
      "find output/* | grep -v mkdocs-material-dib | xargs -n1 rm -fr"

rule process_library:
   input:
      glob.glob('library/*.md'),
      glob.glob('templates/*.md'),
      'templates/mkdocs.yml',
      glob.glob('scripts/*.py')
   output:
      directory('output/docs'),
      'output/mkdocs.yml'
   shell:
      """
      scripts/sed_fixes.sh library
      scripts/process.py library 
      scripts/copy_images.py images
      """

rule mkdocs:
   input:
      'output/docs',
      'output/mkdocs.yml'
   output:
      directory('output/site')
   shell:
      "cd output && {python} -m mkdocs build"

