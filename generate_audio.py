from gtts import gTTS
import os

texts = [
    "Molarity is the number of moles of solute per liter of solution, whereas molality is the number of moles per kilogram of solvent. Because liquids expand when heated, the volume of a solution changes with temperature. Therefore, molarity is temperature-dependent. However, mass is unaffected by heat, making molality entirely independent of temperature.",
    "Both laws state that the partial pressure of a volatile component is directly proportional to its mole fraction. The key difference lies in the proportionality constant. Raoult's law uses the vapor pressure of the pure component, focusing on the solvent. Henry's law uses an empirically determined constant, focusing on the dissolved gas. At very dilute concentrations, the two laws conceptually merge.",
    "An azeotropic mixture is a liquid mixture of two or more components that has a constant boiling point and retains the same composition in both the liquid and vapor phases. A minimum boiling azeotrope, like ethanol and water, boils at a lower temperature than its pure components. A maximum boiling azeotrope, like nitric acid and water, boils at a higher temperature due to stronger molecular interactions.",
    "To find the mole fraction of a 20% ethylene glycol solution, we assume 100 grams of total solution. This gives us 20 grams of ethylene glycol and 80 grams of water. First, convert these masses into moles by dividing by their molar masses. Then, divide the moles of ethylene glycol by the total moles in the solution. The resulting mole fraction is 0.068.",
    "Adding a non-volatile solute lowers the vapor pressure of a solvent. Graphically, this shifts the vapor pressure curve downwards. Because boiling occurs when vapor pressure equals atmospheric pressure, the solution must be heated to a higher temperature to bridge this gap. This increase in temperature is known as boiling point elevation.",
    "Normally, water flows from a lower concentration of solute to a higher one. However, if we apply a pressure greater than the osmotic pressure to the concentrated side, we force the water molecules to move in the opposite direction, leaving the impurities behind. This process is called reverse osmosis, and its most critical application is the desalination of seawater.",
    "The van't Hoff factor, represented by i, is the ratio of the actual number of particles in solution to the number of formula units initially dissolved. It accounts for dissociation or association. For a strong electrolyte like Sodium Chloride, one formula unit completely dissociates into one Sodium ion and one Chloride ion. Therefore, its ideal van't Hoff factor is two.",
    "Freezing point depression is a colligative property, meaning it depends on the number of particles, not their identity. Because glucose has a significantly lower molar mass than cane sugar, a 5% mass solution of glucose contains many more molecules than a 5% mass solution of sugar. More particles lead to a greater depression in the freezing point.",
    "According to Henry's law, the solubility of a gas in a liquid decreases as the temperature increases. In warm water, dissolved oxygen escapes into the atmosphere, leaving less oxygen available for marine life to breathe. Aquatic species feel much more comfortable in cold water because it holds a significantly higher concentration of dissolved oxygen.",
    "Non-ideal solutions do not obey Raoult's law over the entire range of concentrations. When ethanol and acetone are mixed, the acetone molecules break the strong hydrogen bonds between the ethanol molecules. Because the new intermolecular forces are weaker than the original ones, the molecules escape more easily into the vapor phase. This results in a higher vapor pressure, demonstrating a positive deviation from Raoult's law."
]

if not os.path.exists("audio"):
    os.makedirs("audio")

for i, text in enumerate(texts):
    tts = gTTS(text, lang='en')
    tts.save(f"audio/audio_{i+1}.mp3")
    print(f"Generated audio_{i+1}.mp3")
