"""These are macros that can be used in the markdown 

see https://mkdocs-macros-plugin.readthedocs.io/en/latest/macros/
"""
def define_env(env):
  "Hook function"

  @env.macro
  def examplemacro():
      return f"This file is at {env.page.file}"
