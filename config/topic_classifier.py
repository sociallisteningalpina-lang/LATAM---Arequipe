#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""

import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    """
    Retorna una función de clasificación de temas personalizada para campaña Arequipe x LATAM.
    Campaña de activación con Arequipitos Alpina en vuelos de LATAM.
    
    Returns:
        function: Función que toma un comentario (str) y retorna un tema (str)
    
    Usage:
        classifier = create_topic_classifier()
        tema = classifier("El arequipe estaba delicioso en mi vuelo")
        # tema = 'Opinión Positiva - Arequipe/Alpina'
    """
    
    def classify_topic(comment: str) -> str:
        """
        Clasifica un comentario en un tema específico basado en patrones regex.
        
        Args:
            comment: Texto del comentario a clasificar
            
        Returns:
            str: Nombre del tema asignado
        """
        comment_lower = str(comment).lower()
        
        # CATEGORÍA 1: Opinión Positiva - Arequipe/Alpina
        if re.search(
            r'arequipe.*\brico\b|arequipe.*\bdelicioso\b|arequipe.*\bbueno\b|'
            r'arequipe.*\bencanta\b|arequipe.*\bsabroso\b|arequipe.*\bdedo\b|'
            r'alpina.*\brico\b|alpina.*\bbueno\b|me.*encanta.*arequipe',
            comment_lower
        ):
            return 'Opinión Positiva - Arequipe/Alpina'
        
        # CATEGORÍA 2: Opinión Negativa - Arequipe/Alpina
        if re.search(
            r'arequipe.*\bmalo\b|arequipe.*\bazúcar\b|arequipe.*\benfermar\b|'
            r'azúcar.*\barequipe\b|dulce.*exceso|demasiado.*dulce',
            comment_lower
        ):
            return 'Opinión Negativa - Arequipe/Alpina'
        
        # CATEGORÍA 3: Opinión Positiva - LATAM
        if re.search(
            r'latam.*\bmejor\b|latam.*\bbuena\b|latam.*\bexcelente\b|'
            r'latam.*\bencanta\b|latam.*\bnúmero\s*1\b|latam.*\bpreferida\b|'
            r'me\s*l\s*amo.*latam|latam.*detallistas|latam.*atención|'
            r'latam.*seguridad|nunca.*sentido.*bien.*aerolínea',
            comment_lower
        ):
            return 'Opinión Positiva - LATAM'
        
        # CATEGORÍA 4: Opinión Negativa - LATAM
        if re.search(
            r'latam.*\bmierda\b|latam.*\bporquería\b|latam.*\bmala\b|'
            r'latam.*\bpésim[oa]\b|latam.*\broban\b|latam.*\bmaleta\b|'
            r'latam.*\bmalo\b|latam.*control',
            comment_lower
        ):
            return 'Opinión Negativa - LATAM'
        
        # CATEGORÍA 5: Experiencia de Vuelo - Detalles Positivos
        if re.search(
            r'\bdetalle[s]?\b.*\bbonito[s]?\b|\brefrigerio\b|\bcafé\b|'
            r'juan\s*valdez|\batención\b.*\bbuena\b|viajamos.*dieron|'
            r'tripulantes|cabina|clase.*bisnes|business',
            comment_lower
        ):
            return 'Experiencia de Vuelo - Detalles Positivos'
        
        # CATEGORÍA 6: Comparación con Otras Aerolíneas
        if re.search(
            r'\bavianca\b|\biberia\b|otra.*aerolínea|'
            r'mejor.*que.*avianca|decadencia|comparación',
            comment_lower
        ):
            return 'Comparación con Otras Aerolíneas'
        
        # CATEGORÍA 7: Quejas sobre Servicio Aéreo
        if re.search(
            r'roben.*maleta|robar.*equipaje|ni.*tinto.*ofrecen|'
            r'no.*ofrecen|mal.*servicio|equipaje',
            comment_lower
        ):
            return 'Quejas sobre Servicio Aéreo'
        
        # CATEGORÍA 8: Reacciones al Contenido del Video
        if re.search(
            r'el\s*man|video|aparece|charlie\s*kirk|bobo|'
            r'deja.*familia.*perro|jajaja.*arequipe|en\s*serio',
            comment_lower
        ):
            return 'Reacciones al Contenido del Video'
        
        # CATEGORÍA 9: Fuera de Tema / No Relevante
        if re.search(
            r'^jaja+$|^ja+ja+ja+$|^0q|^10\s*q+|^\d+\s*[qa]+\s*\d+|'
            r'^[qoa\s\d]+$|^que\s*bien$|^saludos$',
            comment_lower
        ) or len(comment_lower.split()) < 3:
            return 'Fuera de Tema / No Relevante'
        
        # CATEGORÍA DEFAULT: Otros
        return 'Otros'
    
    return classify_topic

# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
