# build, build and deploy, etc.
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

rule process_library:
   input:
      glob.glob('library/*.md'),
      glob.glob('templates/*.md'),
      'templates/mkdocs.yml'
   output:
      directory('output/docs'),
      'output/mkdocs.yml'
   shell:
      "scripts/process.py library/*.md"

rule mkdocs:
   input:
      'output/docs/',
      'output/mkdocs.yml'
   output:
      directory('output/site')
   shell:
      "cd output && {python} -m mkdocs build"
