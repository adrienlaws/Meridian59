// Meridian 59, Copyright 1994-2012 Andrew Kirmse and Chris Kirmse.
// All rights reserved.
//
// This software is distributed under a license that is described in
// the LICENSE file that accompanies it.
//
// Meridian is a registered trademark.
/*
 * theme.h:  Theme-aware bitmap resource ID lookup for the merintr
 *   module.  Used so bitmap-loading callers can stay theme-blind:
 *   pass the canonical (default-theme) ID and get back the right
 *   variant for the active theme.
 */

#ifndef _MERINTR_THEME_H
#define _MERINTR_THEME_H

int ThemeResourceId(int id);

#endif /* #ifndef _MERINTR_THEME_H */
