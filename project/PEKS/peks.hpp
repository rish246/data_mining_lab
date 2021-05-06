/*
 * peks.h
 *
 *  Created on: Jul 7, 2015
 *      Author: mahind
 */

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <gmp.h>
#include <pbc.h>
#include <assert.h>
#include <openssl/sha.h>

//#define DEBUG 1

/* Apriv = α and Apub  = [g, h=g^α] */
struct key_pub
{
	element_t g;
	element_t h;
};

struct key
{
	element_t priv;
	key_pub pub;
};

/* PEKS = [A, B] i.e. A=g^r and B=H2(t) */
struct peks
{
	element_t A;
	char *B; // PEKS(Apub, Word)
};

void sha512(const char *word, int word_size,
			char hashed_word[SHA512_DIGEST_LENGTH * 2 + 1]);

/*
	Understand get-nbits
*/
void get_n_bits(char *src, char *out, int bitswanted);

void key_printf(key key);

void peks_printf(peks peks);

void init_pbc_param_pairing(pbc_param_t param, pairing_t pairing);


/*
	Bilinear map implementation

	takes a random alpha(privKey) and g(G1) and returns Apub=[g, h = g^alpa], alpha
*/
void KeyGen(key *key, pbc_param_t param, pairing_t pairing);

void PEKS(peks *peks, key_pub *pub, pairing_t pairing,
		  element_t H1_W, int bitswanted);

void Trapdoor(element_t Tw, pairing_t pairing, element_t alpha,
			  element_t H1_W);

int Test(char *W2S, int lenW2S, key_pub *pub, element_t Tw, pairing_t pairing);

int peks_scheme(char *W1, char *W2);
