{
  'targets': [
    {
      'target_name': 'lfs',
      'type': 'shared_library',
      'sources': [
        'src/lfs.c',
        'src/lfs.def',
      ],
      'dependencies': [
        '<(DEPTH)/third_party/lua/lua.gyp:liblua',
      ],
    },
  ],
}
