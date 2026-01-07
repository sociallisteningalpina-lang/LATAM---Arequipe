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
    Retorna una función de clasificación de temas personalizada para la campaña LATAM x Alpina Arequipe.
    
    Returns:
        function: Función que toma un comentario (str) y retorna un tema (str)
    
    Usage:
        classifier = create_topic_classifier()
        tema = classifier("LATAM es la mejor aerolínea")
        # tema = 'Opinión Positiva LATAM'
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
        
        # CATEGORÍA 1: Opinión Positiva LATAM
        if re.search(
            r'latam.{0,20}(mejor|preferid[ao]|encanta|excelente|buena|detallistas|'
            r'n[úu]mero\s*(uno|1)|me\s+amo|bien\s+con)|'
            r'(mejor|preferid[ao]|encanta|excelente|buena).{0,20}latam|'
            r'latan.{0,20}(detallistas|encanta|buena)|'
            r'bonitos?\s+detalles.{0,20}aerol[ií]nea',
            comment_lower
        ):
            return 'Opinión Positiva LATAM'
        
        # CATEGORÍA 2: Opinión Negativa LATAM / Aerolíneas
        if re.search(
            r'latam.{0,20}(mierda|porquer[ií]a|mal[ao]|p[eé]simo)|'
            r'(mierda|porquer[ií]a).{0,20}latam|'
            r'roben\s+la\s+maleta|iberia|avianca.{0,20}(decadencia|mal[ao])|'
            r'ni\s+un\s+tinto\s+ofrecen',
            comment_lower
        ):
            return 'Opinión Negativa LATAM / Aerolíneas'
        
        # CATEGORÍA 3: Opinión Positiva Arequipe Alpina
        if re.search(
            r'arequipe.{0,20}(delicioso|rico|mejor)|'
            r'(delicioso|rico|mejor).{0,20}arequipe|'
            r'alpina\s+es\s+alpina|mejor\s+arequipe|'
            r'no\s+tiene\s+comparaci[oó]n|muy\s+rico|'
            r'necesito\s+la\s+f[aá]brica',
            comment_lower
        ):
            return 'Opinión Positiva Arequipe Alpina'
        
        # CATEGORÍA 4: Comparación / Preferencia Competencia
        if re.search(
            r'alquer[ií]a|proleche|purac[eé]|'
            r'(mejor|sabe\s+mejor).{0,20}(alquer[ií]a|proleche|purac[eé])|'
            r'hay\s+uno\s+que\s+sabe\s+mejor|'
            r'sabe\s+a\s+campo|'
            r'lo\s+compr[oó]\s+alpina.{0,20}(no\s+lo\s+voy|mejor)',
            comment_lower
        ):
            return 'Comparación / Preferencia Competencia'
        
        # CATEGORÍA 5: Crítica Salud / Azúcar
        if re.search(
            r'enfermar|az[uú]car|enfermedades|'
            r'generaci[oó]n.{0,20}(enferm|da[ñn])|'
            r'd[aá]ndole\s+enfermedad',
            comment_lower
        ):
            return 'Crítica Salud / Azúcar'
        
        # CATEGORÍA 6: Humor / Reacción al Contenido
        if re.search(
            r'jaja|🤣|😂|charlie\s+kirk|bobo|backyardigans|'
            r'deja\s+la\s+familia.{0,20}arequipe|'
            r'con\s+el\s+dedo|boca\s+abajo|tapa|'
            r'antojando|antojen|sin\s+plata',
            comment_lower
        ):
            return 'Humor / Reacción al Contenido'
        
        # CATEGORÍA 7: Engagement Positivo Genérico
        if re.search(
            r'qu[eé]\s+bien|👏|👍|😍|🤤|gracias|'
            r'cuando\s+regala|@\w+',
            comment_lower
        ):
            return 'Engagement Positivo Genérico'
        
        # CATEGORÍA 8: Fuera de Tema / No Relevante
        if re.search(
            r'^am[eé]n$|tripulantes\s+de\s+cabina|'
            r'nombre\s+correcto|anuncio\s+favorito|rimas',
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
