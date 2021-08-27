#ifndef __HASH_TABLE_H_
#define __HASH_TABLE_H_

#include <stdint.h>

typedef struct hashNode hashNode;
typedef struct hashTable hashTable;

struct hashNode {
  char *key;
  char *value;
  hashNode *next;
};

struct hashTable {
  hashNode **hashArray;
  uint32_t size;
};

static uint32_t hash_function(const char *key);

static void free_hash_node(hashNode *node);

static void free_list(hashNode *node);

static void free_table(hashTable *table);

static hashNode *create_hash_node(const char *key, const char *value);

hashTable *create_table();

void hash_table_insert(hashTable *table, const char *key, const char *value);

char *hash_table_search(const hashTable *table, const char *key);

void hash_table_delete(hashTable *table, const char *key);

#endif  // __HASH_TABLE_H_
