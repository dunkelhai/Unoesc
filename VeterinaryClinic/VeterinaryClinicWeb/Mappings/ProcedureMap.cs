using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using VeterinaryClinic.BL;

namespace VeterinaryClinicWeb.Mappings
{
    public class ProcedureMap : IEntityTypeConfiguration<Procedure>
    {
        public void Configure(EntityTypeBuilder<Procedure> builder)
        {
            builder.ToTable("Procedure");

            builder.Property(p => p.ProcedureName)
                .HasColumnType("varchar(100)")
                .IsRequired();

            builder.Property(p => p.Observation)
                .HasColumnType("varchar(200)");
        }
    }
}
