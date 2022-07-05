using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using VeterinaryClinic.BL;

namespace VeterinaryClinicWeb.Mappings
{
    public class SpecieMap : IEntityTypeConfiguration<Specie>
    {
        public void Configure(EntityTypeBuilder<Specie> builder)
        {
            builder.ToTable("Specie");

            builder.Property(p => p.Name)
                .HasColumnType("varchar(100)")
                .IsRequired();
        }
    }
}
