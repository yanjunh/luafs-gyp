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
        ['OS == "mac"', {
          'product_prefix': '',
          'product_extension': 'so',
          'xcode_settings': {
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'NO',
          }
        }],
      ]
    },
  ],
}
