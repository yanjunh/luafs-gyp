{
  'targets': [
    {
      'target_name': 'lfs',
      'type': 'shared_library',
      'product_dir': "<(PRODUCT_DIR)",
      'sources': [
        'src/lfs.c',
      ],
      'dependencies': [
        '<(DEPTH)/third_party/lua/lua.gyp:liblua',
      ],
      'conditions': [
        ['OS == "win"', {
          'sources': [
            'src/lfs.def',
          ],
        }],
        ['OS == "linux"', {
          'product_prefix': '',
          'cflags!': ['-fvisibility=hidden'],
        }],
      ]
    },
  ],
}
