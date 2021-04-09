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

uint32_t hash_function(char *key);

hashNode *create_hash_node(char *key, char *value);

hashTable *create_table(uint32_t size);

void free_hash_node(hashNode *node);

void free_table(hashTable *table);

void hashTableInsert(hashTable *table, char *key, char *value);

char *hashTableSearch(hashTable *table, char *key);

void hashTableDelete(hashTable *table, char *key);

#endif // __HASH_TABLE_H_
