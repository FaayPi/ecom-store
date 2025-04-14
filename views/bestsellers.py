import streamlit as st
from typing import Dict, Any, List, Tuple
from neo4j import GraphDatabase
from models.cart import Cart

# Neo4j Connection - verwende die gleichen Credentials wie im Hauptcode
NEO4J_URI = "neo4j+s://5e56b2da.databases.neo4j.io"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "h-jFkG_yO2J_fyusi1QPy6l80eSD_o-dD6tLqC20ePM"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def get_bestsellers(driver) -> Dict[str, str]:
    """
    Ermittelt den Bestseller für jede der Kategorien "Apparel", "Home Goods" und "Electronics"
    """
    category_bestsellers_query = """
    MATCH (p:Product)<-[r:PURCHASED]-()
    WHERE p.category IN ["Apparel", "Home Goods", "Electronics"]
    WITH p.category AS category, p, COUNT(r) AS purchase_count
    ORDER BY category, purchase_count DESC
    WITH category, COLLECT({name: p.name, count: purchase_count})[0] AS top_product
    RETURN category, top_product.name AS product_name
    """
    
    with driver.session() as session:
        result = session.run(category_bestsellers_query)
        # Dictionary mit Kategorie -> Bestseller-Produkt
        category_bestsellers = {record["category"]: record["product_name"] for record in result}
    
    return category_bestsellers

def render_bestsellers(cart, product_map: Dict[str, Any], products):
    """Render bestseller page with the bestselling product for each category"""
    st.title("Category Bestsellers")
    
    # Bestseller nach Kategorien abrufen
    category_bestsellers = get_bestsellers(driver)
    
    if not category_bestsellers:
        st.info("No bestsellers available at the moment.")
        return
    
    # Für jede der drei Kategorien den Bestseller anzeigen
    categories = ["Apparel", "Home Goods", "Electronics"]
    
    for category in categories:
        st.header(f"🏆 Top {category}")
        
        # Prüfen, ob ein Bestseller für diese Kategorie vorhanden ist
        if category not in category_bestsellers:
            st.info(f"No bestseller available for {category} category.")
            continue
        
        # Den Bestseller für diese Kategorie anzeigen
        bestseller = category_bestsellers[category]
        display_product_list([bestseller], products, cart, f"best_{category}")

def display_product_list(product_names: List[str], all_products, cart, prefix=""):
    """Support function to show product overview"""
    for product in all_products:
        if product["Product Name"] in product_names:
            col1, col2 = st.columns([1, 3])
            with col1:
                if product.get('Image'):
                    st.image(product['Image'], width=150)
                else:
                    st.write("No image available")
            
            with col2:
                st.write(f"**{product['Product Name']}**")
                st.write(f"Price: ${product['Price']}")
                if product.get('Description'):
                    st.write(product['Description'])
                
                # Hinzufügen-Button und Mengenauswahl
                col_qty, col_btn = st.columns([1, 2])
                with col_qty:
                    qty = st.number_input(
                        "Quantity",
                        min_value=1,
                        value=1,
                        key=f"{prefix}_qty_{product['Product Name']}",
                        label_visibility="collapsed"
                    )
                with col_btn:
                    if st.button("Add to Cart", key=f"{prefix}_add_{product['Product Name']}"):
                        if "cart_id" in st.session_state:
                            cart.add_item(st.session_state.cart_id, product['Product Name'], qty)
                            st.success(f"Added {qty} {product['Product Name']} to cart")
                            st.rerun()
                        else:
                            st.error("Cart not initialized. Please refresh the page.")
            
            st.write("---")