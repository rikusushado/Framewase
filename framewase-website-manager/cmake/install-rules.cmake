install(
    TARGETS framewase-website-manager_exe
    RUNTIME COMPONENT framewase-website-manager_Runtime
)

if(PROJECT_IS_TOP_LEVEL)
  include(CPack)
endif()
