#include <assert.h>
#include <stdio.h>
#include <string.h>

#include "hash_table.h"

int main(void) {
  printf("---start---\n\n");
  hashTable *table = create_table();
  hash_table_insert(table, "a", "1");
  hash_table_insert(table, "ab", "2");
  hash_table_insert(table, "abc", "3");
  hash_table_insert(table, "abcd", "4");
  hash_table_insert(table, "abcde", "5");
  hash_table_insert(table, "abcdef", "6");
  printf("(key, value) = (\"a\", %s)\n", hash_table_search(table, "a"));
  printf("(key, value) = (\"ab\", %s)\n", hash_table_search(table, "ab"));
  printf("(key, value) = (\"abc\", %s)\n", hash_table_search(table, "abc"));
  printf("(key, value) = (\"abcd\", %s)\n", hash_table_search(table, "abcd"));
  printf("(key, value) = (\"abcde\", %s)\n", hash_table_search(table, "abcde"));
  printf("(key, value) = (\"abcdef\", %s)\n",
         hash_table_search(table, "abcdef"));
  hash_table_delete(table, "a");
  hash_table_delete(table, "ab");
  hash_table_delete(table, "abc");
  hash_table_delete(table, "abcd");
  hash_table_delete(table, "abcde");
  hash_table_delete(table, "abcdef");
  printf("\n---end---\n");
  return 0;
}