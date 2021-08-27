#include "hash_table.h"

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 2000

/* distribution rate is intentional to make its implementation easier */
static uint32_t hash_function(const char *key) {
  uint32_t hashed_val = 0;
  for (size_t i = 0; key[i]; i++) {
    hashed_val += key[i];
  }
  return hashed_val % TABLE_SIZE;
}

static void free_hash_node(hashNode *node) {
  free(node->key);
  free(node->value);
  free(node);
}

static void free_list(hashNode *node) {
  hashNode *current_node;
  while (node != NULL) {
    current_node = node;
    node = node->next;
    free_hash_node(current_node);
  }
}

static void free_table(hashTable *table) {
  for (size_t i = 0; i < table->size; i++) {
    if (table->hashArray[i]) {
      free_list(table->hashArray[i]);
    }
  }
  free(table->hashArray);
  free(table);
}

static hashNode *create_hash_node(const char *key, const char *value) {
  hashNode *node = (hashNode *)malloc(sizeof(hashNode));
  node->key = (char *)malloc(strlen(key) + 1);
  node->value = (char *)malloc(strlen(value) + 1);
  strcpy(node->key, key);
  strcpy(node->value, value);
  return node;
}

hashTable *create_table() {
  hashTable *table = (hashTable *)malloc(sizeof(hashTable));
  table->size = TABLE_SIZE;
  table->hashArray = (hashNode **)calloc(table->size, sizeof(hashNode *));
  for (size_t i = 0; i < table->size; i++) {
    table->hashArray[i] = NULL;
  }
  return table;
}

void hash_table_insert(hashTable *table, const char *key, const char *value) {
  uint32_t index = hash_function(key);
  hashNode *current_node = table->hashArray[index];
  if (current_node == NULL) {
    table->hashArray[index] = create_hash_node(key, value);
  } else {
    while (current_node) {
      current_node = current_node->next;
    }
    current_node = create_hash_node(key, value);
  }
}

char *hash_table_search(const hashTable *table, const char *key) {
  uint32_t index = hash_function(key);
  hashNode *current_node = table->hashArray[index];
  while (true) {
    if (current_node == NULL) {
      return NULL;
    }
    if (strcmp(current_node->key, key) == 0) {
      return current_node->value;
    }
    current_node = current_node->next;
  }
}

void hash_table_delete(hashTable *table, const char *key) {
  uint32_t index = hash_function(key);
  hashNode *current_node = table->hashArray[index];
  // hashArray has only one node
  if (current_node != NULL && current_node->next == NULL) {
    if (strcmp(current_node->key, key) == 0) {
      free_hash_node(current_node);
    }
  }
  // hashArray has multiple nodes
  while (current_node != NULL && current_node->next != NULL) {
    if (strcmp(current_node->next->key, key) == 0) {
      hashNode *tmp_node = current_node->next->next;
      free_hash_node(current_node->next);
      current_node->next = tmp_node;
    }
    current_node = current_node->next;
  }
}
